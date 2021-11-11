from typing import List
from fastapi import APIRouter, Depends, HTTPException
import requests
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from controllers.app_controller import get_all_apps, create_app, get_app_info_by_id, update_app_info, delete_app_info
from controllers.exceptions import AppInfoException
from models.schemas import App, CreateAndUpdateApp, PaginatedAppInfo
from controllers.cve_controller import get_all_cves, create_cve, get_cve_info_by_id, update_cve_info, get_tracked_cves, track_cve
from controllers.exceptions import CveInfoException,CveInfoNotFoundError
from models.schemas import Cve, CreateAndUpdateCve, PaginatedCveInfo
from models.db import get_db
import os
import json
import datetime

NVD_API_KEY = os.environ.get('nvd_api_key')
NVD_API_ENDPOINT = 'https://services.nvd.nist.gov/rest/json'

router = APIRouter()

@router.get("/refresh_cves", response_model=List[Cve])
def refresh_cves(session: Session = Depends(get_db)):

    try:
        apps_list = get_all_apps(session, 1000, 0)
        
        results = []
        for app in apps_list:
            payload = {'apiKey': NVD_API_KEY, 'cpeMatchString': app.cpe, "resultsPerPage":100}
            r = requests.get(f'{NVD_API_ENDPOINT}/cves/1.0/', params=payload)
            new_cves_for_app_data = r.json()['result']['CVE_Items']
            for cve in new_cves_for_app_data:
                cve = cve['cve']
                cve_id = cve['CVE_data_meta']['ID']
                try:
                    x = get_cve_info_by_id(session,cve_id)
                except CveInfoNotFoundError:
                    assigner = cve['CVE_data_meta']['ASSIGNER']
                    description = cve['description']['description_data'][0]['value']
                    impact= cve.get('impact')

                    if impact:
                    
                        if 'baseMetricV3' in impact:
                            severity = impact['baseMetricV3']['cvssV3']['baseSeverity']
                            attack_vector = impact['baseMetricV3']['cvssV3']['attackVector']
                            confidentiality_impact = impact['baseMetricV3']['cvssV3']['confidentialityImpact']
                            integrity_impact = impact['baseMetricV3']['cvssV3']['integrityImpact']
                            availability_impact = impact['baseMetricV3']['cvssV3']['availabilityImpact']
                        
                        elif 'baseMetricV2' in impact:
                            severity = impact['baseMetricV2']['severity']
                            attack_vector = impact['baseMetricV2']['cvssV2']['accessVector']
                            confidentiality_impact = impact['baseMetricV2']['cvssV2']['confidentialityImpact']
                            integrity_impact = impact['baseMetricV2']['cvssV2']['integrityImpact']
                            availability_impact = impact['baseMetricV2']['cvssV2']['availabilityImpact']
                        
                    else:
                        severity = ''
                        attack_vector = ''
                        confidentiality_impact = ''
                        integrity_impact = ''
                        availability_impact = ''

                    external_links = [link["url"] for link in cve['references']['reference_data'][:10]]
                    published_date = str(datetime.datetime.now())
                    if cve.get('publishedDate'):
                        published_date = cve['publishedDate']
                    
                    last_modified_date = str(datetime.datetime.now())
                    if cve.get('lastModifiedDate'):
                        last_modified_date = cve['lastModifiedDate']
                    tracked = 0

                    new_cve = CreateAndUpdateCve(
                        cve_id = cve_id,
                        assigner = assigner,
                        description = description,
                        severity = severity,
                        attack_vector = attack_vector,
                        confidentiality_impact = confidentiality_impact,
                        integrity_impact = integrity_impact,
                        availability_impact = availability_impact,
                        external_links = external_links,
                        published_date = published_date,
                        last_modified_date = last_modified_date,
                        tracked = tracked
                    )

                    try:
                        cve_info = create_cve(session, new_cve)
                        results.append(cve_info)

                    except:
                        pass

        return results
    
    except Exception as e:
        raise


@router.get("/track_cve/{cve_id}", response_model=Cve)
def track_cve_by_id(cve_id: int, session: Session = Depends(get_db)):

    try:
        cve_info = track_cve(session, cve_id)
        return cve_info
    except CveInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.get("/tracked_cves", response_model=List[Cve])
def tracked_cves(session:Session = Depends(get_db)):

    cves_list = get_tracked_cves(session)

    return cves_list
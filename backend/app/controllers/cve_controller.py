from typing import List
from sqlalchemy.orm import Session
from models.schemas import Cve
from .exceptions import CveInfoInfoAlreadyExistError, CveInfoNotFoundError
from models.models import CveInfo
from models.schemas import CreateAndUpdateCve


def get_all_cves(session: Session, limit: int, offset: int) -> List[CveInfo]:
    return session.query(CveInfo).offset(offset).limit(limit).all()

def get_cve_info_by_id(session: Session, _id: int) -> CveInfo:
    cve_info = session.query(CveInfo).get(_id)

    if cve_info is None:
        raise CveInfoNotFoundError

    return cve_info

def get_tracked_cves(session: Session) -> List[CveInfo]:
    cve_info = session.query(CveInfo).filter(CveInfo.tracked == True).all()
    return cve_info


def create_cve(session: Session, cve_info: CreateAndUpdateCve) -> CveInfo:
    cve_details = session.query(CveInfo).filter(
        CveInfo.cve_id == cve_info.cve_id,
        ).first()
    
    if cve_details is not None:
        raise CveInfoInfoAlreadyExistError

    new_cve_info = CveInfo(**cve_info.dict())
    session.add(new_cve_info)
    session.commit()
    session.refresh(new_cve_info)
    return new_cve_info


def update_cve_info(session: Session, _id: int, info_update: CreateAndUpdateCve) -> CveInfo:
    cve_info = get_cve_info_by_id(session, _id)

    if cve_info is None:
        raise CveInfoNotFoundError

    cve_info.cve_id = info_update.cve_id 
    cve_info.assigner = info_update.assigner 
    cve_info.description = info_update.description 
    cve_info.severity = info_update.severity 
    cve_info.attack_vector = info_update.attack_vector
    cve_info.confidentiality_impact = info_update.confidentiality_impact 
    cve_info.integrity_impact = info_update.integrity_impact 
    cve_info.availability_impact = info_update.availability_impact 
    cve_info.external_links = info_update.external_links 
    cve_info.published_date = info_update.published_date
    cve_info.last_modified_date = info_update.last_modified_date
    cve_info.tracked = info_update.tracked


    session.commit()
    session.refresh(cve_info)

    return cve_info

def delete_cve_info(session: Session, _id: int):
    cve_info = get_cve_info_by_id(session, _id)

    if cve_info is None:
        raise CveInfoNotFoundError

    session.delete(cve_info)
    session.commit()

    return

def track_cve(session: Session, _id: int) -> CveInfo:
    cve_info = get_cve_info_by_id(session, _id)

    if cve_info is None:
        raise CveInfoNotFoundError

   
    cve_info.tracked = 1


    session.commit()
    session.refresh(cve_info)

    return cve_info

def delete_cve_info(session: Session, _id: int):
    cve_info = get_cve_info_by_id(session, _id)

    if cve_info is None:
        raise CveInfoNotFoundError

    session.delete(cve_info)
    session.commit()

    return
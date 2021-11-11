from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from controllers.cve_controller import get_all_cves, create_cve, get_cve_info_by_id, update_cve_info, delete_cve_info
from models.db import get_db
from controllers.exceptions import CveInfoException
from models.schemas import Cve, CreateAndUpdateCve, PaginatedCveInfo

router = APIRouter()

@cbv(router)
class Cves:
    session: Session = Depends(get_db)

    # API to get the list of cve info
    @router.get("/cves", response_model=PaginatedCveInfo)
    def list_cves(self, limit: int = 10, offset: int = 0):

        cves_list = get_all_cves(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": cves_list}

        return response

    # API endpoint to add a cve info to the database
    @router.post("/cves")
    def add_cve(self, cve_info: CreateAndUpdateCve):

        try:
            cve_info = create_cve(self.session, cve_info)
            return cve_info
        except CveInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular cve
@router.get("/cves/{cve_id}", response_model=Cve)
def get_cve_info(cve_id: int, session: Session = Depends(get_db)):

    try:
        cve_info = get_cve_info_by_id(session, cve_id)
        return cve_info
    except CveInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing cve info
@router.put("/cves/{cve_id}", response_model=Cve)
def update_cve(cve_id: int, new_info: CreateAndUpdateCve, session: Session = Depends(get_db)):

    try:
        cve_info = update_cve_info(session, cve_id, new_info)
        return cve_info
    except CveInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a cve info from the data base
@router.delete("/cves/{cve_id}")
def delete_cve(cve_id: int, session: Session = Depends(get_db)):

    try:
        return delete_cve_info(session, cve_id)
    except CveInfoException as cie:
        raise HTTPException(**cie.__dict__)
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from controllers.app_controller import get_all_apps, create_app, get_app_info_by_id, update_app_info, delete_app_info
from db import get_db
from controllers.exceptions import AppInfoException
from models.schemas import App, CreateAndUpdateApp, PaginatedAppInfo

router = APIRouter()

@cbv(router)
class Apps:
    session: Session = Depends(get_db)

    # API to get the list of app info
    @router.get("/apps", response_model=PaginatedAppInfo)
    def list_apps(self, limit: int = 10, offset: int = 0):

        apps_list = get_all_apps(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": apps_list}

        return response

    # API endpoint to add a app info to the database
    @router.post("/apps")
    def add_app(self, app_info: CreateAndUpdateApp):

        try:
            app_info = create_app(self.session, app_info)
            return app_info
        except AppInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular app
@router.get("/apps/{app_id}", response_model=App)
def get_app_info(app_id: int, session: Session = Depends(get_db)):

    try:
        app_info = get_app_info_by_id(session, app_id)
        return app_info
    except AppInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing app info
@router.put("/apps/{app_id}", response_model=App)
def update_app(app_id: int, new_info: CreateAndUpdateApp, session: Session = Depends(get_db)):

    try:
        app_info = update_app_info(session, app_id, new_info)
        return app_info
    except AppInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a app info from the data base
@router.delete("/apps/{app_id}")
def delete_app(app_id: int, session: Session = Depends(get_db)):

    try:
        return delete_app_info(session, app_id)
    except AppInfoException as cie:
        raise HTTPException(**cie.__dict__)
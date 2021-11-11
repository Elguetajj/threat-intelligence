from typing import List
from sqlalchemy.orm import Session
from models.schemas import App
from .exceptions import AppInfoInfoAlreadyExistError, AppInfoNotFoundError
from models.models import AppInfo
from models.schemas import CreateAndUpdateApp


def get_all_apps(session: Session, limit: int, offset: int) -> List[AppInfo]:
    return session.query(AppInfo).offset(offset).limit(limit).all()

def get_app_info_by_id(session: Session, _id: int) -> AppInfo:
    app_info = session.query(AppInfo).get(_id)

    if app_info is None:
        raise AppInfoNotFoundError

    return app_info

def create_app(session: Session, app_info: CreateAndUpdateApp) -> AppInfo:
    app_details = session.query(AppInfo).filter(
        AppInfo.app_cpe == app_info.app_cpe,
        AppInfo.os_cpe == app_info.os_cpe
        ).first()
    
    if app_details is not None:
        raise AppInfoInfoAlreadyExistError

    new_app_info = AppInfo(**app_info.dict())
    session.add(new_app_info)
    session.commit()
    session.refresh(new_app_info)
    return new_app_info

def update_app_info(session: Session, _id: int, info_update: CreateAndUpdateApp) -> AppInfo:
    app_info = get_app_info_by_id(session, _id)

    if app_info is None:
        raise AppInfoNotFoundError

    app_info.name = info_update.name
    app_info.cpe = info_update.cpe

    session.commit()
    session.refresh(app_info)

    return app_info

def delete_app_info(session: Session, _id: int):
    app_info = get_app_info_by_id(session, _id)

    if app_info is None:
        raise AppInfoNotFoundError

    session.delete(app_info)
    session.commit()

    return
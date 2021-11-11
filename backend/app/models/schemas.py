from pydantic import BaseModel
from typing import Optional, List


class CreateAndUpdateApp(BaseModel):
    name : str 
    os_cpe : str 
    app_cpe : str

class App(CreateAndUpdateApp):
    id: int
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class PaginatedAppInfo(BaseModel):
    limit: int
    offset: int
    data: List[App]



class CreateAndUpdateCve(BaseModel):
    cve_id : str
    assigner : str
    description : str
    severity : str
    confidentiality_impact : str
    integrity_impact : str
    availability_impact : str
    external_links : str

class Cve(CreateAndUpdateCve):
    id: int

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class PaginatedCveInfo(BaseModel):
    limit: int
    offset: int
    data: List[Cve]




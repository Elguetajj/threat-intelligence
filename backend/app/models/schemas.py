from datetime import datetime
from pydantic import BaseModel

from typing import Optional, List

from pydantic.types import Json


class CreateAndUpdateApp(BaseModel):
    name : str 
    cpe : str 

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
    attack_vector: str
    confidentiality_impact : str
    integrity_impact : str
    availability_impact : str  
    external_links : Optional[List[str]]        
    published_date: datetime
    last_modified_date: datetime
    tracked: Optional[bool]

class Cve(CreateAndUpdateCve):
    id: int

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

class PaginatedCveInfo(BaseModel):
    limit: int
    offset: int
    data: List[Cve]




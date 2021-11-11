from pydantic.types import Json
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import JSON, Boolean, DateTime
from sqlalchemy.types import String, Integer, Enum
from .db import Base
import enum

class AppInfo(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cpe = Column(String)
    created = Column(DateTime)

# CREATE TABLE apps (
# 	id INTEGER NOT NULL AUTO_INCREMENT, 
# 	`name` VARCHAR(100),
# 	`os_cpe` VARCHAR(100) ,
# 	`app_cpe` VARCHAR(100),
#     created TIMESTAMP,
# 	PRIMARY KEY (id)
# );

class CveInfo(Base):
    __tablename__ = "tracked_cves"

    id = Column(Integer, primary_key=True, index=True)
    cve_id = Column(String)
    assigner = Column(String)
    description = Column(String)
    severity = Column(String)
    attack_vector = Column(String)
    confidentiality_impact = Column(String)
    integrity_impact = Column(String)
    availability_impact = Column(String)
    external_links = Column(JSON)
    published_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    tracked = Column(Boolean)
    created = Column(DateTime)


# CREATE TABLE tracked_cves(
# 	id INTEGER NOT NULL AUTO_INCREMENT, 
# 	`cve_id` VARCHAR(100),
# 	`assigner` VARCHAR(100) ,
# 	`description` TEXT,
# 	`severity` VARCHAR(100),
# 	`attack_vector` VARCHAR(100),
# 	`confidentiality_impact` VARCHAR(100),
# 	`integrity_impact` VARCHAR(100),
# 	`availability_impact` VARCHAR(100),
# 	`external_links` JSON,
# 	'published_date' TIMESTAMP ,
# 	'last_modified_date' TIMESTAMP,
#     created TIMESTAMP,
# 	PRIMARY KEY (id)

# );

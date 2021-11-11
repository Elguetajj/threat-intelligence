from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.types import String, Integer, Enum
from .db import Base
import enum

class AppInfo(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    os_cpe = Column(String)
    app_cpe = Column(String)
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
    confidentiality_impact = Column(String)
    integrity_impact = Column(String)
    availability_impact = Column(String)
    external_links = Column(String)
    created = Column(DateTime)


# CREATE TABLE tracked_cves(
# 	id INTEGER NOT NULL AUTO_INCREMENT, 
# 	`cve_id` VARCHAR(100),
# 	`assigner` VARCHAR(100) ,
# 	`description` TEXT,
#     created TIMESTAMP,
# 	PRIMARY KEY (id)

# );
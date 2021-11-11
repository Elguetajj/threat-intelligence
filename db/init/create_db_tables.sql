CREATE DATABASE configs;
USE configs;

CREATE TABLE apps (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	`name` VARCHAR(100),
	`os_cpe` VARCHAR(100) ,
	`app_cpe` VARCHAR(100),
    created TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE tracked_cves(
	id INTEGER NOT NULL AUTO_INCREMENT, 
	`cve_id` VARCHAR(100),
	`assigner` VARCHAR(100) ,
	`description` TEXT,
	`severity` VARCHAR(100),
	`confidentiality_impact` VARCHAR(100),
	`integrity_impact` VARCHAR(100),
	`availability_impact` VARCHAR(100),
	`external_links` VARCHAR(100),
    created TIMESTAMP,
	PRIMARY KEY (id)

);
-- class App(Base):
--     id = Column(Integer, primary_key=True, index=True)
--     cve_id = Column(String)
--     assigner = Column(String)
--     description = Column(String)
--     severity = Column(String)
--     confidentiality_impact = Column(String)
--     integrity_impact = Column(String)
--     availability_impact = Column(String)
--     external_links = Column(String)
--     created = Column(DateTime)
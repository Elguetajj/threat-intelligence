CREATE DATABASE configs;
USE configs;


CREATE TABLE apps (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	`name` VARCHAR(100),
	`cpe` VARCHAR(100) ,
    created TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (id)
);

CREATE TABLE tracked_cves(
	id INTEGER NOT NULL AUTO_INCREMENT, 
	`cve_id` VARCHAR(100),
	`assigner` VARCHAR(100) ,
	`description` TEXT,
	`severity` VARCHAR(100),
	`attack_vector` VARCHAR(100),
	`confidentiality_impact` VARCHAR(100),
	`integrity_impact` VARCHAR(100),
	`availability_impact` VARCHAR(100),
	`external_links` JSON,
	`published_date` DATETIME NULL DEFAULT NULL ,
	`last_modified_date` DATETIME NULL DEFAULT NULL,
	created TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (id)

);



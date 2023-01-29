DROP TABLE IF EXISTS Sales_Word_Count, Community_Services_Word_Count, Healthcare_Word_Count, Construction_Word_Count, Engineering_Word_Count, All_Fields_Word_Count;
DROP TABLE IF EXISTS Construction_Location_Count, Engineering_Location_Count, Healthcare_Location_Count, Sales_Location_Count, Community_Services_Location_Count;
DROP TABLE IF EXISTS Construction_Scrapes, Engineering_Scrapes, Healthcare_Scrapes, Sales_Scrapes, Community_Service_Scrapes;
DROP TABLE IF EXISTS Job_ID CASCADE;


-- Create tables for SCRAPED DATA

-- JOB_ID

CREATE TABLE Job_ID (
	job_id INT PRIMARY KEY NOT NULL,
	job_field VARCHAR,
	job_location VARCHAR
);

-- CONSTRUCTION_SCRAPES

CREATE TABLE Construction_Scrapes (
	job_id INT,
	job_title TEXT,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- ENGINEERING_SCRAPES

CREATE TABLE Engineering_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- HEALTHCARE_SCRAPES

CREATE TABLE Healthcare_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- SALES_SCRAPES

CREATE TABLE Sales_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- COMMUNITY_SERVICES_SCRAPES

CREATE TABLE Community_Service_Scrapes (
	job_id INT,
	job_title VARCHAR,
	company_name VARCHAR,
	short_description TEXT,
	job_location VARCHAR,
	job_classification VARCHAR,
	job_subclassification VARCHAR,
	job_site VARCHAR(20),
	FOREIGN KEY (job_id) REFERENCES Job_ID(job_id)
);

-- Create tables for LOCATION COUNT

CREATE TABLE Construction_Location_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	count INT
);

CREATE TABLE Engineering_Location_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	count INT
);

CREATE TABLE Healthcare_Location_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	count INT
);

CREATE TABLE Sales_Location_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	count INT
);

CREATE TABLE Community_Services_Location_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	count INT
);

-- Create tables for WORD COUNT

CREATE TABLE Sales_Word_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	word VARCHAR(25),
	count INT
);

CREATE TABLE Community_Services_Word_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	word VARCHAR(25),
	count INT
);

CREATE TABLE Healthcare_Word_Count (
	job_field VARCHAR(30),
	job_location VARCHAR(30),
	word VARCHAR(15),
	count INT
);

CREATE TABLE Construction_Word_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	word VARCHAR(25),
	count INT
);

CREATE TABLE Engineering_Word_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	word VARCHAR(25),
	count INT
);

CREATE TABLE All_Fields_Word_Count (
	job_field VARCHAR,
	job_location VARCHAR,
	word VARCHAR(25),
	count INT
);
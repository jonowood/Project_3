CREATE TABLE "Jora_Scrape" (
	"Industry" VARCHAR NOT NULL,
	"job_title" VARCHAR NOT NULL,
	"company_name" VARCHAR NOT NULL,
	"short_description" VARCHAR NOT NULL
);

CREATE TABLE "Jora_Word_Count" (
	"words" VARCHAR NOT NULL,
	"count" INT NOT NULL
);

-- drop table "Jora_Word_Count";
-- drop table "Jora_Scrape";
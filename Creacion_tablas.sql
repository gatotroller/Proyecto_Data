DROP TABLE IF EXISTS IndustryTable;

CREATE TABLE IndustryTable(
	industry_id INT IDENTITY(1,1),
	industry_name NVARCHAR(255)
);

DROP TABLE IF EXISTS RoleTable;

CREATE TABLE RoleTable(
	role_id INT IDENTITY(1,1),
	role_name NVARCHAR(255)
);

INSERT INTO IndustryTable (industry_name)
SELECT DISTINCT industry
FROM trabajos2.dbo.jobs_data;

INSERT INTO RoleTable (role_name)
SELECT DISTINCT role
FROM trabajos2.dbo.jobs_data;

DROP TABLE IF EXISTS SkillsTable;

SELECT *
INTO SkillsTable
FROM trabajos2.dbo.data_skills;

DROP TABLE IF EXISTS JobsData;

SELECT *
INTO JobsData
FROM trabajos2.dbo.jobs_data;

ALTER TABLE JobsData
ADD industry_id INT,
    role_id INT;

UPDATE jd
SET jd.industry_id = it.industry_id
FROM JobsData jd
	JOIN IndustryTable it ON jd.industry = it.industry_name;

UPDATE jd
SET jd.role_id = rt.role_id
FROM JobsData jd 
	JOIN RoleTable rt ON jd.role = rt.role_name;

ALTER TABLE JobsData
DROP COLUMN industry,
			role;
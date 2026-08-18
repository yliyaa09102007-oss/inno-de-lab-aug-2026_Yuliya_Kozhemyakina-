--increasing all HRs salary
UPDATE employeesdata.employees 
SET salary = salary*1.1
WHERE department = 'HR';

-- IT --> Senior IT, where salary>70000
UPDATE employeesdata.employees 
SET department = 'Senior IT'
WHERE salary>=70000 AND department = 'IT';

--deleting employees, who is not assinged to any projects
DELETE FROM employeesdata.employees AS e
WHERE NOT EXISTS (
	SELECT 1
	FROM employeesdata.employeeprojects e2
	WHERE e.employeeid = e2.employeeid
)

--transaction (adding a project and assinging employees to it)
BEGIN;

INSERT INTO employeesdata.projects (projectname, budget, startdate, enddate)
VALUES
	('Game Development', 300000, '2025-12-15', '2026-12-15')			
ON CONFLICT (projectid) DO NOTHING
RETURNING projectid;

INSERT INTO employeesdata.employeeprojects (employeeid, projectid, hoursworked)
VALUES
	(2, 4, 100),
	(4, 4, 135)
ON CONFLICT (employeeid, projectid) DO NOTHING; 

COMMIT;
--selecting all projects where Bob Johnson worked more than 150h
SELECT 
	p.projectname, 
	e.firstname, --also added these three columns to be sure
	e.lastname,
	ep.hoursworked
FROM employeesdata.projects AS p
LEFT JOIN employeesdata.employeeprojects AS ep	--left joining two tables to get a full table with all columns
	ON p.projectid=ep.projectid
LEFT JOIN employeesdata.employees AS e
	ON ep.employeeid = e.employeeid 
WHERE e.firstname = 'Bob' 
	AND e.lastname = 'Johnson' 
	AND ep.hoursworked >= 150;

--updating budget
UPDATE employeesdata.projects p 
SET budget=budget*1.1
WHERE EXISTS (
    SELECT 1
    FROM employeesdata.employeeprojects ep
    INNER JOIN employeesdata.employees e 
    	ON ep.employeeid = e.employeeid 
    WHERE ep.projectid = p.projectid
    AND (e.department = 'IT' OR e.department = 'Senior IT')
);

--setting EndDate
--I'm adding a new line because i dont have any projects without enddate (to see results)
INSERT INTO employeesdata.projects (projectid, projectname, budget, startdate, enddate)
VALUES (5, 'AI development', 250000, '2026-02-26', NULL)
ON CONFLICT (projectid) DO NOTHING;

UPDATE employeesdata.projects
SET enddate = startdate + INTERVAL '1 year'
WHERE enddate IS NULL;

SELECT * FROM employeesdata.projects p;

--adding a new employee and assinging him to a project
ROLLBACK;
BEGIN;
	INSERT INTO employeesdata.employees (employeeid, firstname, lastname, department, salary)
	VALUES		
		(5, 'Kirill', 'Ivanov', 'Finance', 57000.00)
	ON CONFLICT (employeeid) DO NOTHING
	RETURNING employeeid; --getting ID (only when adding for the first time bc if "ON CONFLICT DO NOTHING")
	
	INSERT INTO employeesdata.employeeprojects (employeeid, projectid, hoursworked)
	SELECT 
    	5, p.projectid, 80
	FROM employeesdata.projects p
	WHERE p.projectname = 'Website Redesign'
	ON CONFLICT (employeeid, projectid) DO NOTHING;
COMMIT;

SELECT * FROM employeesdata.employeeprojects e;

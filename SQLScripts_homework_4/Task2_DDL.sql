SET search_path TO employeesdata, public;

--I'm adding "If not exists" so I can run my code multiple times while I add new lines
CREATE TABLE IF NOT EXISTS Departments (
	DepartmentID SERIAL PRIMARY KEY,
	DepartmentName VARCHAR(50) UNIQUE NOT NULL,
	Locationn VARCHAR(50)
);

ALTER TABLE employees ADD COLUMN IF NOT EXISTS email VARCHAR(100);

UPDATE employees 
SET email = LOWER(firstname || '.' || lastname || employeeid || '@gmail.com');
--now every employee has it's own unique email based on name and id (cuz i'm lazy)

--adding a constraint
ALTER TABLE employees ADD CONSTRAINT UQ_email UNIQUE(email);

--renaming Locationn
ALTER TABLE departments RENAME COLUMN Locationn TO OfficeLocation;
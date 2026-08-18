SET search_path TO employeesdata, public;   --redirecting my commands to a different schema "employeesdata"

--the first command
INSERT INTO employees (firstname, lastname, department, salary)
VALUES
	--listing all the values needed to be added according to their type
	('Yuliya', 'Kozhemyakina', 'SMM', 90000.00),			--but i wanna work as an IT specialist *cry emoji*
	('Natalya', 'Kozhemyakina', 'Finance', 91000.00)
ON CONFLICT (employeeid) DO NOTHING; 						--so i can run all commands without error messages

--the second command
SELECT * FROM employees AS e;

--the third command (listing all the employees who work in IT)
SELECT 
	firstname,
	lastname,
	department
FROM employees AS e
WHERE department = 'IT';

--the fourth command (updating salary)
UPDATE employees 
SET salary = 65000
WHERE firstname = 'Alice' AND lastname = 'Smith';

--the fifth command (Deleting Eve)
DELETE FROM employees
WHERE firstname = 'Eve' AND lastname = 'Davis';

--the last command (checking)
SELECT * FROM employees AS e
ORDER BY e.employeeid;

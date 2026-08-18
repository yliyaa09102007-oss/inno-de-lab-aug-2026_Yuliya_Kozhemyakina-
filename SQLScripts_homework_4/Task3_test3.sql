INSERT INTO employeesdata.employees (firstname, lastname, department, salary)
VALUES
	('Nastya', 'Goncharova', 'IT', 51000.00);

UPDATE employeesdata.employees 
SET salary = 85000
WHERE firstname = 'Yuliya' AND lastname = 'Kozhemyakina';

SELECT * FROM employeesdata.employees;
	
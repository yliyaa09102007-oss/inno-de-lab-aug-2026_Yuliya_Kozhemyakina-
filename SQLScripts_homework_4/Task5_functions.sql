--a function to calculate bonus (not sure why employeeid has to be there)

CREATE OR REPLACE FUNCTION CalculateAnnualBonus(eid integer, esalary NUMERIC)
RETURNS NUMERIC AS $$
DECLARE
	bonus NUMERIC;
BEGIN
	bonus=esalary*0.1;
	RETURN bonus;
END;
$$ LANGUAGE plpgsql;

--select + previous function

SELECT
	e.employeeid,
	e.firstname,
	e.lastname,
	e.salary,
	CalculateAnnualBonus(e.employeeid, e.salary) AS bonus
FROM employeesdata.employees e;

--creating a view


CREATE OR REPLACE VIEW IT_Department_View
AS
	SELECT
		e.employeeid,
		e.firstname,
		e.lastname,
		e.salary,
		e.department --not in the hometask, but added to be sure
	FROM employeesdata.employees AS e
	WHERE department = 'IT' OR 
	      department = 'Senior IT'; --added it, because in my table there is no employees with department 'IT'

SELECT * FROM IT_Department_View;
	
	
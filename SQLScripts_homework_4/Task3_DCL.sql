CREATE USER hr_user WITH PASSWORD '123123';
GRANT USAGE ON SCHEMA employeesdata TO hr_user;
GRANT SELECT ON employeesdata.employees TO hr_user;
SELECT current_user;

--the second part
GRANT INSERT, UPDATE ON employeesdata.employees TO hr_user;
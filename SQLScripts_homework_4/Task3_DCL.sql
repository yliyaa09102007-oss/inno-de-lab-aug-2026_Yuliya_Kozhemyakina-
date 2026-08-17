CREATE USER hr_user1 WITH PASSWORD '123123';
GRANT USAGE ON SCHEMA employeesdata TO hr_user1;
GRANT SELECT ON employeesdata.employees TO hr_user1;
SELECT current_user;

--the second part
GRANT INSERT, UPDATE ON employeesdata.employees TO hr_user1;
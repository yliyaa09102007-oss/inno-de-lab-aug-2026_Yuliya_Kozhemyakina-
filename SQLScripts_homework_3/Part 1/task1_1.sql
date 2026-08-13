SELECT 
	first_name,
	last_name,
	age,
	country
FROM customers AS o
WHERE age>25 AND country='USA'
	
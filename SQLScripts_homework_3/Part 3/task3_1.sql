SELECT
	country,
	count(*)
FROM customers AS c
GROUP BY country

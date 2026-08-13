SELECT
	c.first_name,
	c.last_name,
	o.amount
FROM customers AS c
INNER JOIN orders AS o
	ON c.customer_id = o.customer_id 
	WHERE o.amount = (
		SELECT MAX(amount)
		FROM orders
	)
SELECT 
	c.first_name,
	c.last_name,
	o.item,
	o.amount
FROM orders AS o							--orders in this case is the main table, and we join customers to it
LEFT JOIN customers AS c
	ON c.customer_id = o.customer_id    	--joining by field "customer_id"
ORDER BY c.first_name, o.order_id 
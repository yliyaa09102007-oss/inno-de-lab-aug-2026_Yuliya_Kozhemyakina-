SELECT
	s.status,
	c.first_name,
	c.last_name,
	o.item
FROM shippings AS s
LEFT JOIN customers AS c
	ON s.customer = c.customer_id
INNER JOIN orders AS o
	ON c.customer_id = o.customer_id 

-- I added "item" from "orders", because I think it's kind of important to see which item is being delivered
-- Not sure if I did it right though
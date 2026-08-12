SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,  	--using concat to merge two columns into one
	c.country,
	COUNT(o.order_id) AS total_orders,					  	--counting amount of orders
	SUM(o.amount) AS total_amount							--counting total amount
FROM customers AS c
INNER JOIN orders AS o
	ON c.customer_id = o.customer_id
INNER JOIN shippings AS s
	ON c.customer_id = s.customer
--finding customers with >=2 orders
WHERE c.customer_id IN (
	SELECT customer_id
	FROM orders
	GROUP BY customer_id
	HAVING count(order_id)>=2
)
--also finding customers who have at least 1 order with status "Delivered"
AND c.customer_id IN(
	SELECT customer
	FROM shippings
	WHERE status = 'Delivered'
)
GROUP BY c.customer_id
ORDER BY total_orders
SELECT 
	item,
	count(*),
	AVG(amount) AS avg_amount
FROM orders AS o
GROUP BY o.item
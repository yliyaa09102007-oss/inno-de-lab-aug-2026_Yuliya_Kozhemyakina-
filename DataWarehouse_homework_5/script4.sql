--shows how did revenue and the number of appointments change over the years

SELECT
	d.Year,
	SUM(f.TotalCost) AS Revenue,
	COUNT(f.FactID) AS AppointmentsCount
FROM FactAppointments AS f
INNER JOIN DimDate AS d ON f.DateID = d.DateID
GROUP BY d.Year
ORDER BY d.Year DESC;
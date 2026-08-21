--shows the months which have the peak number of visits 
--we don't need the year there, because we don't want the analysis of which year brought the most revenue in this case

SELECT 
    d.Month,
    COUNT(f.FactID) AS AppointmentsCount,
    SUM(f.TotalCost) AS Revenue,
    AVG(f.TotalCost) AS AvgCheck
FROM FactAppointments AS f
INNER JOIN DimDate AS d ON f.DateID = d.DateID
GROUP BY d.Month
ORDER BY appointmentscount, d.Month;
--which day of the week is the most busy?

SELECT 
    d.DayOfTheWeek,
    COUNT(f.FactID) AS AppointmentsCount,
    SUM(f.TotalCost) AS Revenue,
    AVG(f.TotalCost) AS AvgCheck
FROM FactAppointments AS f
INNER JOIN DimDate AS d ON f.DateID = d.DateID
GROUP BY d.DayOfTheWeek
ORDER BY appointmentscount DESC;
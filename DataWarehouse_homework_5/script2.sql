--which services are in highest demand?
--also we can change "ORDER BY TotalRevenue" to "ORDER BY AvgCheck" to get the information about the most expencive type of service

SELECT 
    st.ServiceName,
    st.ServiceCategory,
    COUNT(f.FactID) AS AppointmentsCount,
    SUM(f.TotalCost) AS TotalRevenue,
    AVG(f.TotalCost) AS AvgCheck,
    AVG(f.Duration) AS AvgDurationMin
FROM FactAppointments AS f
INNER JOIN DimServiceType AS st ON f.ServiceTypeSK = st.ServiceTypeSK
GROUP BY st.ServiceTypeID, st.ServiceName, st.ServiceCategory
ORDER BY totalrevenue DESC;
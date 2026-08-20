--which pets visit the clinic most often?
--also we can change "ORDER BY AppointmentCount" to "ORDER BY AvgCheck" to get the information about the most profitable pet species

SELECT 
    sp.SpeciesName,
    COUNT(f.FactID) AS AppointmentsCount,
    SUM(f.TotalCost) AS TotalRevenue,
    AVG(f.TotalCost) AS AvgCheck,
    AVG(f.Duration) AS AvgDurationMin
FROM FactAppointments AS f
INNER JOIN DimPets AS p ON f.PetID = p.PetID
INNER JOIN DimSpecies AS sp ON p.SpeciesID = sp.SpeciesID
GROUP BY sp.SpeciesID, sp.SpeciesName
ORDER BY appointmentscount DESC;
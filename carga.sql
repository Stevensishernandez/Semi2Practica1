
Bulk insert temp 

From 'C:\Users\Steven Sis\Desktop\All\Vacas Diciembre 2021\Semi 2\Lab\Practica1\tsunami historical data from 1800 to 2021.csv'

With(
Firstrow = 3,
FIELDTERMINATOR = ',' , 
ROWTERMINATOR = '\n'
);


INSERT INTO TsunamiCauseCode(idTsunamiCauseCode,name)
SELECT DISTINCT Tsunami_Cause_Code,'default' FROM temp WHERE Tsunami_Cause_Code IS NOT NULL;


INSERT INTO TsunamiEventValidity(idTsunamiEventValidity,name)
SELECT DISTINCT Tsunami_Event_Validity,'default' FROM temp WHERE Tsunami_Event_Validity IS NOT NULL;


INSERT INTO dbo.Date (Year,Mo,Dy)
SELECT DISTINCT Year,Mo,Dy FROM temp;


INSERT INTO dbo.location (Country,LocationName)
SELECT DISTINCT Country,Location_Name FROM temp;

TRUNCATE TABLE  Position;
INSERT INTO dbo.Position (Latitude,Longitude)
SELECT DISTINCT Latitude,Longitude FROM temp ;


INSERT INTO dbo.Event (idDate, idLocation, idPosition, MaximumWaterHeight, NumberofRunups,TsunamiMagnitude, TsunamiIntensity, Hr, Mn, Sec, TotalDeaths, TotalMissing, TotalMissingDescription,
						TotalInjuries,TotalDamage,TotalDamageDescription, TotalHousesDestroyed, TotalHousesDamaged, idTsunamiCauseCode, idTsunamiEventValidity )
(SELECT D.idDate, L.idLocation, P.idPosition, T.Maximum_Water_Height, T.Number_of_Runups, T.Tsunami_Magnitude, T.Tsunami_Intensity, T.Hr, T.Mn, T.Sec,
	T.Total_Deaths, T.Total_Missing, T.Total_Missing_Description, T.Total_Injuries, T.Total_Damage, T.Total_Damage_Description, T.Total_Houses_Destroyed, T.Total_Houses_Damaged,
	T.Tsunami_Cause_Code, T.Tsunami_Event_Validity
	FROM Date D, Location L, temp T, Position P 
WHERE ( (T.Mo = D.Mo OR  (T.Mo IS NULL AND D.Mo IS NULL)) and (T.Dy = D.Dy OR (T.Dy IS NULL AND D.Dy IS NULL) ) AND T.Year = D.Year) AND 
	  ((L.Country = T.Country OR  (L.Country IS NULL AND T.Country IS NULL) ) and (L.LocationName = T.Location_Name OR  (L.LocationName IS NULL AND T.Location_Name IS NULL))) AND
	  ((P.Latitude = T.Latitude OR  (P.Latitude IS NULL AND T.Latitude IS NULL) ) and (P.Longitude = T.Longitude OR  (P.Longitude IS NULL AND T.Longitude IS NULL))));

-- Consulta 1
SELECT
                QUOTENAME(SCHEMA_NAME(sOBJ.schema_id)) + '.' + QUOTENAME(sOBJ.name) AS [TableName]
                , SUM(sdmvPTNS.row_count) AS [RowCount]
            FROM
                sys.objects AS sOBJ
                INNER JOIN sys.dm_db_partition_stats AS sdmvPTNS
                        ON sOBJ.object_id = sdmvPTNS.object_id
            WHERE 
                sOBJ.type = 'U'
                AND sOBJ.is_ms_shipped = 0x0
                AND sdmvPTNS.index_id < 2
            GROUP BY
                sOBJ.schema_id
                , sOBJ.name
            ORDER BY [TableName]

-- Cosulta 2
SELECT * FROM (
	SELECT D.Year, L.Country, ROW_NUMBER() OVER(Partition by D.Year ORDER BY L.Country) AS Row_Number FROM Event E
	INNER JOIN Location L ON (L.idLocation=E.idLocation)
	INNER JOIN Date D ON (D.idDate=E.idDate)
	GROUP BY L.Country, D.Year
) S
pivot(
	max(Country)
	for [Row_Number] in ([1],[2],[3],[4],[5])
) P
-- Consulta 3

SELECT * FROM (
	SELECT L.Country, D.Year, ROW_NUMBER() OVER(Partition by L.Country ORDER BY D.Year) AS Row_Number FROM Event E
	INNER JOIN Location L ON (L.idLocation=E.idLocation)
	INNER JOIN Date D ON (D.idDate=E.idDate) 
	GROUP BY D.Year, L.Country
) S
pivot(
	max(Year)
	for [Row_Number] in ([1],[2],[3],[4],[5])
) P

-- Consulta 4
SELECT L.Country, AVG(E.TotalDamage) as Promedio FROM Event E
INNER JOIN Location L ON (L.idLocation = E.idLocation)
GROUP BY L.Country
HAVING AVG(E.TotalDamage) > 0
ORDER BY Promedio  DESC

-- Consulta 5
SELECT TOP 5 L.Country, SUM(E.TotalDeaths) Total FROM Event E
INNER JOIN Location L ON (L.idLocation = E.idLocation)
GROUP BY L.Country
ORDER BY Total  DESC

-- Consulta 6
SELECT TOP 5 D.Year, SUM(E.TotalDeaths) Total FROM Event E
INNER JOIN Date D ON (D.idDate = E.idDate)
GROUP BY D.Year
ORDER BY Total DESC

-- Consulta 7
SELECT TOP 5 D.Year, COUNT(*) Total FROM Event E
INNER JOIN Date D ON (D.idDate = E.idDate)
GROUP BY D.Year
ORDER BY Total DESC

-- Consulta 8
SELECT TOP 5 L.Country, SUM(E.TotalHousesDestroyed) Total FROM Event E
INNER JOIN Location L ON (L.idLocation = E.idLocation)
GROUP BY L.Country
ORDER BY Total  DESC

-- Consulta 9
SELECT TOP 5 L.Country, SUM(E.TotalHousesDamaged) Total FROM Event E
INNER JOIN Location L ON (L.idLocation = E.idLocation)
GROUP BY L.Country
ORDER BY Total  DESC

-- Consulta 10
SELECT L.Country, AVG(E.MaximumWaterHeight) Total FROM Event E
INNER JOIN Location L ON (L.idLocation = E.idLocation)
GROUP BY L.Country
HAVING SUM(E.MaximumWaterHeight) > 0
ORDER BY Total  DESC
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-A4PU5CM\SQLEXPRESS;'
                      'Database=SoulHealer_201800484;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#Example * Select
cursor.execute('SELECT * FROM Genero')
for i in cursor:
    print(i)

#Example Create Table

#cursor.execute('''
#		CREATE TABLE products (
#			product_id int primary key,
#			product_name nvarchar(50),
#			price int
#			)
#              ''')

#Example Create Temp
# cursor.execute('''
# 		CREATE TABLE temp (
# 			Year varchar(50),
# 			Mo varchar(50),
# 			Dy varchar(50),
# 			Hr varchar(50),
# 			Mn varchar(50),
# 			Sec varchar(50),
# 			Tsunami_Event_Validity varchar(50),
# 			Tsunami_Cause_Code varchar(50),
# 			Earthquake_Magnitude varchar(50),
# 			Deposits varchar(50),
# 			Country varchar(50),
# 			Location_Name varchar(50),
# 			Latitude varchar(50),
# 			Longitude varchar(50),
# 			Maximum_Water_Height varchar(50),
# 			Number_of_Runups varchar(50),
# 			Tsunami_Magnitude varchar(50),
# 			Tsunami_Intensity varchar(50),
# 			Total_Deaths varchar(50),
# 			Total_Missing varchar(50),
# 			Total_Missing_Description varchar(50),
# 			Total_Injuries varchar(50),
# 			Total_Damage  varchar(50),
# 			Total_Damage_Description varchar(50),
# 			Total_Houses_Destroyed varchar(50),
# 			Total_Houses_Damaged  varchar(50)
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE TsunamiCauseCode (
# 			idTsunamiCauseCode int PRIMARY KEY,
# 			name varchar(50)
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE TsunamiEventValidity (
# 			idTsunamiEventValidity int PRIMARY KEY,
# 			name varchar(50)
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE Date (
# 			idDate INT IDENTITY(1,1) PRIMARY KEY,
# 			Mo INT NULL,
#             Dy INT NULL,
#             Year INT NULL
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE Location (
# 			idLocation INT IDENTITY(1,1) PRIMARY KEY,
# 			Country varchar(50) NULL,
#             LocationName varchar(50) NULL
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE Position (
# 			idPosition INT IDENTITY(1,1) PRIMARY KEY,
# 			Latitude float NULL,
#             Longitude float NULL
# 			)
#              ''')

# cursor.execute('''
# 		CREATE TABLE Event (
# 			idEvent INT IDENTITY(1,1) PRIMARY KEY,
# 			MaximumWaterHeight float NULL,
#             NumberofRunups INT NULL,
#             TsunamiMagnitude float NULL,
#             TsunamiIntensity float NULL,
#             TotalDeaths float NULL,
#             TotalMissing float NULL,
#             TotalMissingDescription float NULL,
#             TotalInjuries float NULL,
#             TotalDamage float NULL,
#             TotalDamageDescription float NULL,
#             TotalHousesDestroyed float NULL,
#             TotalHousesDamaged float NULL,
#             Hr float NULL,
#             Mn float NULL,
#             Sec float NULL,
#             idPosition INT NULL,
#             idTsunamiCauseCode INT NULL,
#             idTsunamiEventValidity INT NULL,
#             idDate INT NULL,
#             idLocation INT NULL,
#             FOREIGN KEY (idPosition) REFERENCES Position(idPosition),
#             FOREIGN KEY (idTsunamiCauseCode) REFERENCES TsunamiCauseCode(idTsunamiCauseCode),
#             FOREIGN KEY (idTsunamiEventValidity) REFERENCES TsunamiEventValidity(idTsunamiEventValidity),
#             FOREIGN KEY (idDate) REFERENCES Date(idDate),
#             FOREIGN KEY (idLocation) REFERENCES Location(idLocation)
            
# 			)
#              ''')

#Example Carga masiva
# s = ''' Bulk insert temp From 
#         'C:\\Users\\Steven Sis\\Desktop\\All\\Vacas Diciembre 2021\\Semi 2\\Lab\\Practica1\\tsunami historical data from 1800 to 2021.csv' 
#         With( Firstrow = 3,        
#         FIELDTERMINATOR = ',' ,  
#         ROWTERMINATOR = '\\n'  ); '''
# cursor.execute(s)

#Example llenar tablas
# cursor.execute('''
# 		INSERT INTO TsunamiCauseCode(idTsunamiCauseCode,name)
#         SELECT DISTINCT Tsunami_Cause_Code,'default' FROM temp WHERE Tsunami_Cause_Code IS NOT NULL;
#              ''')

# cursor.execute('''
# 		INSERT INTO TsunamiEventValidity(idTsunamiEventValidity,name)
#         SELECT DISTINCT Tsunami_Event_Validity,'default' FROM temp WHERE Tsunami_Event_Validity IS NOT NULL;
#              ''')

# cursor.execute('''
#             INSERT INTO dbo.Date (Year,Mo,Dy)
#             SELECT DISTINCT Year,Mo,Dy FROM temp;
#               ''')

# cursor.execute('''
#             INSERT INTO dbo.location (Country,LocationName)
#             SELECT DISTINCT Country,Location_Name FROM temp;
#               ''')



# cursor.execute('''
#             INSERT INTO dbo.Position (Latitude,Longitude)
#             SELECT DISTINCT Latitude,Longitude FROM temp WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL;
#               ''')

cursor.execute('''
            INSERT INTO dbo.Event (idDate, idLocation, idPosition, MaximumWaterHeight, NumberofRunups,TsunamiMagnitude, TsunamiIntensity, Hr, Mn, Sec, TotalDeaths, TotalMissing, TotalMissingDescription,
			TotalInjuries,TotalDamage,TotalDamageDescription, TotalHousesDestroyed, TotalHousesDamaged, idTsunamiCauseCode, idTsunamiEventValidity )
            (SELECT D.idDate, L.idLocation, P.idPosition, T.Maximum_Water_Height, T.Number_of_Runups, T.Tsunami_Magnitude, T.Tsunami_Intensity, T.Hr, T.Mn, T.Sec,
                T.Total_Deaths, T.Total_Missing, T.Total_Missing_Description, T.Total_Injuries, T.Total_Damage, T.Total_Damage_Description, T.Total_Houses_Destroyed, T.Total_Houses_Damaged,
                T.Tsunami_Cause_Code, T.Tsunami_Event_Validity
                FROM Date D, Location L, temp T, Position P 
            WHERE ( (T.Mo = D.Mo OR  (T.Mo IS NULL AND D.Mo IS NULL)) and (T.Dy = D.Dy OR (T.Dy IS NULL AND D.Dy IS NULL) ) AND T.Year = D.Year) AND 
                ((L.Country = T.Country OR  (L.Country IS NULL AND T.Country IS NULL) ) and (L.LocationName = T.Location_Name OR  (L.LocationName IS NULL AND T.Location_Name IS NULL))) AND
                ((P.Latitude = T.Latitude OR  (P.Latitude IS NULL AND T.Latitude IS NULL) ) and (P.Longitude = T.Longitude OR  (P.Longitude IS NULL AND T.Longitude IS NULL))));
              ''')


conn.commit()
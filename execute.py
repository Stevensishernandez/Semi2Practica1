import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-A4PU5CM\SQLEXPRESS;'
                      'Database=Semi2P1;'
                      'Trusted_Connection=yes;')

def createModel():
    
    cursor = conn.cursor()
# #Example * Select
# cursor.execute('SELECT * FROM Genero')
# for i in cursor:
#     print(i)                

#Example Create Temp
    cursor.execute('''
            CREATE TABLE temp (
                Year varchar(50),
                Mo varchar(50),
                Dy varchar(50),
                Hr varchar(50),
                Mn varchar(50),
                Sec varchar(50),
                Tsunami_Event_Validity varchar(50),
                Tsunami_Cause_Code varchar(50),
                Earthquake_Magnitude varchar(50),
                Deposits varchar(50),
                Country varchar(50),
                Location_Name varchar(50),
                Latitude varchar(50),
                Longitude varchar(50),
                Maximum_Water_Height varchar(50),
                Number_of_Runups varchar(50),
                Tsunami_Magnitude varchar(50),
                Tsunami_Intensity varchar(50),
                Total_Deaths varchar(50),
                Total_Missing varchar(50),
                Total_Missing_Description varchar(50),
                Total_Injuries varchar(50),
                Total_Damage  varchar(50),
                Total_Damage_Description varchar(50),
                Total_Houses_Destroyed varchar(50),
                Total_Houses_Damaged  varchar(50)
                )
                ''')

    cursor.execute('''
            CREATE TABLE TsunamiCauseCode (
                idTsunamiCauseCode int PRIMARY KEY,
                name varchar(50)
                )
                ''')

    cursor.execute('''
            CREATE TABLE TsunamiEventValidity (
                idTsunamiEventValidity int PRIMARY KEY,
                name varchar(50)
                )
                ''')

    cursor.execute('''
            CREATE TABLE Date (
                idDate INT IDENTITY(1,1) PRIMARY KEY,
                Mo INT NULL,
                Dy INT NULL,
                Year INT NULL
                )
                ''')

    cursor.execute('''
            CREATE TABLE Location (
                idLocation INT IDENTITY(1,1) PRIMARY KEY,
                Country varchar(50) NULL,
                LocationName varchar(50) NULL
                )
                ''')

    cursor.execute('''
            CREATE TABLE Position (
                idPosition INT IDENTITY(1,1) PRIMARY KEY,
                Latitude float NULL,
                Longitude float NULL
                )
                ''')

    cursor.execute('''
            CREATE TABLE Event (
                idEvent INT IDENTITY(1,1) PRIMARY KEY,
                MaximumWaterHeight float NULL,
                NumberofRunups INT NULL,
                TsunamiMagnitude float NULL,
                TsunamiIntensity float NULL,
                TotalDeaths float NULL,
                TotalMissing float NULL,
                TotalMissingDescription float NULL,
                TotalInjuries float NULL,
                TotalDamage float NULL,
                TotalDamageDescription float NULL,
                TotalHousesDestroyed float NULL,
                TotalHousesDamaged float NULL,
                Hr float NULL,
                Mn float NULL,
                Sec float NULL,
                idPosition INT NULL,
                idTsunamiCauseCode INT NULL,
                idTsunamiEventValidity INT NULL,
                idDate INT NULL,
                idLocation INT NULL,
                FOREIGN KEY (idPosition) REFERENCES Position(idPosition),
                FOREIGN KEY (idTsunamiCauseCode) REFERENCES TsunamiCauseCode(idTsunamiCauseCode),
                FOREIGN KEY (idTsunamiEventValidity) REFERENCES TsunamiEventValidity(idTsunamiEventValidity),
                FOREIGN KEY (idDate) REFERENCES Date(idDate),
                FOREIGN KEY (idLocation) REFERENCES Location(idLocation)
                
                )
                ''')
    conn.commit()
    print('   -* Model was created')

def deleteModel():
    cursor = conn.cursor()

    cursor.execute('''
            DROP TABLE Event;
            DROP TABLE Date;
            DROP TABLE Location;
            DROP TABLE Position;
            DROP TABLE temp;
            DROP TABLE TsunamiCauseCode;
            DROP TABLE TsunamiEventValidity;
                ''')
    conn.commit()
    print('   -* Model was deleted')

def uploadDate():
    inputS = input()
    cursor = conn.cursor()
#Example Carga masiva
    s = """ Bulk insert temp From '"""
    s+=inputS
    s += """' 
            With( Firstrow = 3,        
            FIELDTERMINATOR = ',' ,  
            ROWTERMINATOR = '\\n'  ); """
    cursor.execute(s)

#Example llenar tablas
    cursor.execute('''
            INSERT INTO TsunamiCauseCode(idTsunamiCauseCode,name)
            SELECT DISTINCT Tsunami_Cause_Code,'default' FROM temp WHERE Tsunami_Cause_Code IS NOT NULL;
                ''')

    cursor.execute('''
            INSERT INTO TsunamiEventValidity(idTsunamiEventValidity,name)
            SELECT DISTINCT Tsunami_Event_Validity,'default' FROM temp WHERE Tsunami_Event_Validity IS NOT NULL;

                ''')

    cursor.execute('''
                INSERT INTO dbo.Date (Year,Mo,Dy)
                SELECT DISTINCT Year,Mo,Dy FROM temp;
                ''')

    cursor.execute('''
                INSERT INTO dbo.location (Country,LocationName)
                SELECT DISTINCT Country,Location_Name FROM temp;
                ''')



    cursor.execute('''
                INSERT INTO dbo.Position (Latitude,Longitude)
                SELECT DISTINCT Latitude,Longitude FROM temp ;
                ''')

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
    print('   -* Model was uploaded')

menu_options2 = {
    1: 'Query 1',
    2: 'Query 2',
    3: 'Query 3',
    4: 'Query 4',
    5: 'Query 5',
    6: 'Query 6',
    7: 'Query 7',
    8: 'Query 8',
    9: 'Query 9',
    10: 'Query 10',
    11: 'Exit',
}

def print_menu():
    for key in menu_options2.keys():
        print (key, '--', menu_options2[key] )

def querysMake():
    query = ''
    cursor = conn.cursor()
# #Example * Select
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:
        query = ''' 
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
        '''
    elif option == 2:
        query = ''' 
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
        '''
    elif option == 3:
        query = ''' 
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
        '''
    elif option == 4:
        query = ''' 
            SELECT L.Country, AVG(E.TotalDamage) as Promedio FROM Event E
            INNER JOIN Location L ON (L.idLocation = E.idLocation)
            GROUP BY L.Country
            HAVING AVG(E.TotalDamage) > 0
            ORDER BY Promedio  DESC
        '''
    elif option == 5:
        query = ''' 
            SELECT TOP 5 L.Country, SUM(E.TotalDeaths) Total FROM Event E
            INNER JOIN Location L ON (L.idLocation = E.idLocation)
            GROUP BY L.Country
            ORDER BY Total  DESC
        '''
    elif option == 6:
        query = ''' 
            SELECT TOP 5 D.Year, SUM(E.TotalDeaths) Total FROM Event E
            INNER JOIN Date D ON (D.idDate = E.idDate)
            GROUP BY D.Year
            ORDER BY Total DESC
        '''
    elif option == 7:
        query = ''' 
            SELECT TOP 5 D.Year, COUNT(*) Total FROM Event E
            INNER JOIN Date D ON (D.idDate = E.idDate)
            GROUP BY D.Year
            ORDER BY Total DESC
        '''
    elif option == 8:
        query = ''' 
            SELECT TOP 5 L.Country, SUM(E.TotalHousesDestroyed) Total FROM Event E
            INNER JOIN Location L ON (L.idLocation = E.idLocation)
            GROUP BY L.Country
            ORDER BY Total  DESC
        '''
    elif option == 9:
        query = ''' 
            SELECT TOP 5 L.Country, SUM(E.TotalHousesDamaged) Total FROM Event E
            INNER JOIN Location L ON (L.idLocation = E.idLocation)
            GROUP BY L.Country
            ORDER BY Total  DESC
        '''
    elif option == 10:
        query = ''' 
            SELECT L.Country, AVG(E.MaximumWaterHeight) Total FROM Event E
            INNER JOIN Location L ON (L.idLocation = E.idLocation)
            GROUP BY L.Country
            HAVING SUM(E.MaximumWaterHeight) > 0
            ORDER BY Total  DESC
        '''
    elif option == 11:
        print('  --*Exit menu')
    else:
        print('Invalid option. Please enter a number between 1 and 4.')

    cursor.execute(query)
    print(' ')
    for i in cursor:
        print(i)    
    print(' ')

    
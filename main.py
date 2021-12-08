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

#Example Carga masiva
s = ''' Bulk insert temp From 'C:\Users\Steven Sis\Desktop\All\Vacas Diciembre 2021\Semi 2\Lab\Practica1\\tsunami historical data from 1800 to 2021.csv' With( Firstrow = 3,        FIELDTERMINATOR = ',' ,  ROWTERMINATOR = '\\n's  ); '''
cursor.execute('''
		CREATE TABLE products2 (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
             ''')
conn.commit()
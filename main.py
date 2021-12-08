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

conn.commit()
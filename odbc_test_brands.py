"""
odbc test
"""
import pyodbc

# connection info
server = 'sql.wrangle.works'
database = 'IESA'
username = 'stacy'
password = '8d39c!76b8d1'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# cursor info
cursor = connection.cursor()

# query info
brand_query = ['''
    SELECT DISTINCT Brand
    FROM ProductsClean
    WHERE ProductCategory = 'FluidPower'
    ORDER BY Brand DESC
    ''']
brand_array = []

# print each row as delimitted record
cursor.execute(brand_query[0]) # reset the cursor
row = cursor.fetchone()
while row:
    for i in row:
        print('{}'.format(i), end='')
        brand_array.append(i)

    row = cursor.fetchone()
    print('')

#for brand in brand_array:
#    print(brand)

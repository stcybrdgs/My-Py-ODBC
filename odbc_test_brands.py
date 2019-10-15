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
q1 = ['''
    SELECT TOP 10 *
    FROM ProductsClean
    WHERE ProductCategory = \'Electrical\'
    ''']
q2 = ['''
    SELECT TOP 10 *
    FROM ProductsClean
    WHERE ProductCategory = \'PPE\'
    ''']

sql_queries = [ q1[0], q2[0] ]

# print each row as list to console
for query in sql_queries:
    cursor.execute(query)
    for row in cursor:
        print(row)

# print each row as delimitted record
cursor.execute(q2[0]) # reset the cursor
row = cursor.fetchone()
while row:
    for i in row:
        print('{} | '.format(i), end='')
    row = cursor.fetchone()
    print('')

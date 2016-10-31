import pymssql
import csv
conn = pymssql.connect(server='tia33kx9ix.database.windows.net', user='the_force@tia33kx9ix', password='abc123!@#', database='students')
cursor = conn.cursor()
csvfile1 = open('./tempFinalFood.csv', 'rb')
reader = csv.reader(csvfile1, delimiter=',', quotechar='|')
i = 0
result = []
x = []
for row in reader:
    try:
        x = [row[0], row[2], row[1], row[40]]
        result.append(tuple(x))
    except:
        pass
#print result
cursor.executemany(
    "INSERT INTO [codefundoforce].[FinalData] VALUES (%s,%s,%s,%s)",
     result)       
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()
"""
try:
	row = cursor.fetchall()
	while row:
	    print row[0] + " " + str(row[1]) + " " + str(row[2])   
	    row = cursor.fetchone()
except:
	print "Exception occured"
"""
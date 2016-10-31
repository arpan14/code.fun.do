import pymssql
conn = pymssql.connect(server='tia33kx9ix.database.windows.net', user='the_force@tia33kx9ix', password='abc123!@#', database='students')
cursor = conn.cursor()
#cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')

cursor.executemany(
    "INSERT INTO [codefundoforce].[inter] VALUES (%s, %d, %d, %d, %d,%d)",
    [('hn Smith', 1, 2, 3, 4, 1),
     ('ne Doe',4,1, 2, 3, 4),
     ('ike T.',1, 2, 3, 4, 1),
     ('pan T.',1, 2, 3, 4, 1),
     ('bil T.',1, 2, 3, 4, 1)])
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
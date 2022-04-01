import psycopg2

conn = psycopg2.connect(
   database="DAC_Backend", user='postgres', password='@123', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from dac'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  user="app1user",
  database="app1",
  password="student"
)

print("Pripojeno.")

cursor = connection.cursor()
query = "insert into package(name) values (%s)"
values = ['balicek']
cursor.execute(query, values)
connection.commit()
query = "select * from package"
cursor.execute(query)
records = cursor.fetchall()
query = "select count(id) from package"
cursor.execute(query)
records = cursor.fetchall()

connection.close()

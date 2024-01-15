import cx_Oracle

connection = cx_Oracle.connect(user="APLIKACE1", password="student", dsn="127.0.0.1/xepdb1", encoding="UTF-8")

print("Pripojeno.")

connection.close()

import mysql.connector
mysq = mysql.connector.connect(host="localhost",
user="root",
password = "afsaneh75",
database = "Paradise"
)

mycursor = mysq.cursor()
sql = "DELETE FROM customers name"
mycursor.execute(sql)

mysq.commit()

print(mycursor.rowcount, "record(s) deleted!")

import mysql.connector
mysq = mysql.connector.connect(host="localhost",
user="root",
password = "afsaneh75",
database = "Paradise"
)

mycursor = mysq.cursor()

sql = " DROP TABLE customers "
mycursor.execute(sql)

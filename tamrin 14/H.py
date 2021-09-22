import mysql.connector
mysq = mysql.connector.connect(host="localhost",
user="root",
password = "afsaneh75",
database = "Paradise"
)

mycursor = mysq.cursor()

sql = " DROP DATABASE Paradise "
mycursor.execute(sql)

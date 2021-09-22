import mysql.connector

mysq =mysql.connector.connect(host="localhost",user="root",password="afsaneh75",database="Paradise")
mycursor=mysq.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
for i in myresult:
    print(i)

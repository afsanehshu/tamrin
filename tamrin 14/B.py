import mysql.connector

mysq =mysql.connector.connect(host="localhost",user="root",password="afsaneh75",database="Paradise")
mycursor=mysq.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)



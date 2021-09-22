import mysql.connector

mysq = mysql.connector.connect(host="localhost",user="root",password="afsaneh75",database="Paradise")

mycursor = mysq.cursor()
mycursor.execute("CREATE TABLE customers(name VARCHAR(255) ,age VARCHAR(255))")
                 

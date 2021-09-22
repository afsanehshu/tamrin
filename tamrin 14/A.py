import mysql.connector

mysq = mysql.connector.connect(host="localhost",user="root",password="afsaneh75")

mycursor = mysq.cursor()
mycursor.execute("CREATE DATABASE Paradise")

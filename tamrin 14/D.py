import mysql.connector

mysq = mysql.connector.connect(host="localhost",user="root",password="afsaneh75",database="Paradise")
mycursor=mysq.cursor()
sql = "INSERT INTO customers(name ,age) VALUES (%s,%s)"
val = [ ("arsam" ,"25"),
        ('ali' ,'20'),
        ('nilu' ,'23'),
        ('mobin','24')
        ]
mycursor.executemany(sql,val)
mysq.commit()

print(mycursor.rowcount,'mas inserted.')

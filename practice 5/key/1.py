import datetime

time = datetime.datetime.today().minute

if (time%7)%2 == 0:
     print("Even")

else:
     print("odd")

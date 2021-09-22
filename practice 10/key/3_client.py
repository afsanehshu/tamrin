from socket import *
import subprocess as sub


s = socket(2,1)
s.connect(("127.0.0.1", 23455))

data = s.recv(1024).decode()

if data == "1":
     sub.check_output("SHUTDOWN /S /t 30", shell = True)
     s.send("Done!".encode())
elif data == "2":
     sub.check_output("SHUTDOWN /r /t 30", shell = True)
     s.send("Done!".encode())
else:
     s.send("Valid Number".encode())
     

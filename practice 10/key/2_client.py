from socket import *


s = socket(2,1)
s2 = socket(2,1)

s.connect(("127.0.0.1", 23455))

ip = s.recv(1024).decode()
port = s.recv(1024).decode()


try:
     s2.connect((ip,int(port)))
     s.send("open".encode())

except:
     s.send("close".encode())

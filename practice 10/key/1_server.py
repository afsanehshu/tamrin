from socket import *


s = socket(2, 1)

s.bind(("127.0.0.1", 23455))
s.listen(1)

c, addr = s.accept()

c.send("Hello Iam Server".encode())
data = c.recv(1024).decode()

print(data)

c.close()
s.close()

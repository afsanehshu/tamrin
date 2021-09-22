from socket import *


s = socket(2,1)
s.bind(("127.0.0.1", 23455))
s.listen(1)

c,addr = s.accept()


ip= input("ip= ")
port= input("port= ")

print()
c.send(ip.encode())
c.send(port.encode())
print("Done!")
print()

data = c.recv(1024).decode()
print(data)


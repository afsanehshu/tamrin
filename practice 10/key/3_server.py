from socket import *

s = socket(2,1)
s.bind(("127.0.0.1", 23455))
s.listen(1)

c, addr = s.accept()

print("1: SHUTDOWN")
print("2: RESTRAT")

print()

CH = input("Enter your choice : ")
c.send(CH.encode())

data = c.recv(1024).decode()
print(data)

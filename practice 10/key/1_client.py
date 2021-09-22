from socket import *
import subprocess as sub

s = socket(2, 1)

s.connect(("127.0.0.1", 23455))

data = s.recv(1024).decode()
print(data)

cmd = sub.check_output("ipconfig", shell=True)
s.send(cmd)

s.close()


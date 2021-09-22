import subprocess as sub
import os


passwand = ["txt", "exe", "pdf", "xlsx", "rar"]
sys_drive=[]

def Find_Drive():
     drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]

     cmd = sub.check_output("net share",shell=True).decode()
     
     for i in drive:
         if i in str(cmd):
             sys_drive.append(i)


def Create_Folder():
     try:
          os.mkdir("Backup")
     except FileExistsError:
          print("\nExist")


def Find_File():
     for i in sys_drive:
          for j in passwand:
              try:
                  cmd = sub.check_output("dir/ S/ B "+i+"\\"+File+"."+j, shell=True).decode()
                  F.write(str(cmd))
              except sub.CalledProcessError:
                  pass

def Copy_File():
     for i in range(10):
         try:
             sub.check_output("copy "+str(F1.readline().strip())+" .\Backup", shell=True).decode()
         except:
             pass




File = input("Enter File Name: ")
Find_Drive()
Create_Folder()
F = open("./Backup/Backup.txt", "w")
Find_File()
F.close()
F1 = open("./Backup/Backup.txt", "r")
Copy_File()
F1.close

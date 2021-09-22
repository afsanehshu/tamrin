N_Stu = int(input("Enter Number Of Student: "))
print()

File = open("Max.txt", "w")
File_1 = open("Failed.txt", "w")
File_2 = open("Passed.txt", "w")

Dict = {}
for i in range(N_Stu):
     Name = input("Enter Name Of Student: ")
     
     while True:
          Mark = int(input("Enter Mark Of Student: "))
          if Mark < 0 or Mark > 100:
               print("Value Error Try Again")
          else:
               break
          
     Dict[Name] = {}
     Dict[Name]["Mark"] = Mark
     print("______________________")


for i in Dict:   
     if Dict[i]["Mark"] == 100:
          File.write(str((i, Dict[i]["Mark"])))
          File_2.write(str((i, Dict[i]["Mark"])))
        
     elif Dict[i]["Mark"] < 70:
          File_1.write(str((i, Dict[i]["Mark"])))

     elif Dict[i]["Mark"] >= 70:
          File_2.write(str((i, Dict[i]["Mark"])))


File.close()
File_1.close()
File_2.close()

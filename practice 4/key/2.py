Dict_List = {}


FName_1 = input("Enter FName_1 : ")
LName_1 = input("Enter LName_1 : ")
Job_1 = input("Enter job_1 : ")

Dict_List["Brad"]={"FName" : FName_1,
                   "LName" : LName_1,
                   "Job" : Job_1}


print("\n")


FName_2 = input("Enter FName_2 : ")
LName_2 = input("Enter LName_2 : ")
Job_2 = input("Enter job_2 : ")

Dict_List["Samyar"]={"FName" : FName_2,
                   "LName" : LName_2,
                   "Job" : Job_2}


print("\n")

print("Brad",Dict_List["Brad"])
print("Samyar",Dict_List["Samyar"])




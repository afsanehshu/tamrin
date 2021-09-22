stu = int(input("Enter num of student : "))

print()

Dict_List = {}
Dict_List_2 = {}
Max = 0

for i in range(stu):
     name = input("Enter name of student : ")
     number = int(input("Enter number : "))
     mid = int(input("Enter mid : "))

     Dict_List[i] = {"Name" : name,
                     "number" : number,
                     "mid" : mid}

     if mid > Max:
          Max = mid
          new_num = number
          new_name = name

          Dict_List_2[new_num] = {"Name" : new_name,
                                   "mid" : Max}
          
     elif mid == Max:
          Max = mid
          new_num = number
          new_name = name

          Dict_List_2[new_num] = {"Name" : new_name,
                                   "mid" : Max}

print(Dict_List_2)

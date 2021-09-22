List = [False, True, 5, "5", "Ali Norouzi", 25.5]

print("Len : ",len(List),"\t", "Type : ",type(List),"\n")

List.extend(["Python","Programming"])

List.insert(len(List)-1,"Python Enginnering")

print(List)

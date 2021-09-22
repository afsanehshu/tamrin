List = []

for i in range(5):
     num = float(input("Enter float Num : "))
     List.append(num)

     
print()
List.sort()
L = List[::-1]
print("sort List : ",L)

print()
print("mid : ",sum(L)/5)

Max=L[0]
Min=L[4]

print("max : ",Max)
print("min : ",Min)

print()

print("List : ",tuple(L))

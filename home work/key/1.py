'''

from collections import Counter

String = input("Enter : ")

S = list(String)

S1 = Counter(S)

print(S1)

'''



'''

String = input("Enter : ")
print(String.count('a'))


v = "abcdefghijklmnopqrstuvwxyz"
String = input("Enter : ")

for i in v:
  count = String.count(i)
  print (i, count)

'''

'''

String = input("Enter : ")

Dict = {}

for i in String:
     if i in Dict:
          Dict[i]+=1
     else:
          Dict[i]=1
print(Dict)

'''


















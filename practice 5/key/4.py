def lower(obj):
     d = {"lower_case":0}
     for i in obj:
          if i.islower():
               d["lower_case"]+=1
     print(d)
     

def upper(obj):
     d = {"upper_case":0}
     for i in obj:
          if i.isupper():
               d["upper_case"]+=1
     print(d)
     

def digit(obj):
     d = {"digit":0}
     for i in obj:
          if i.isdigit():
               d["digit"]+=1
     print(d)



String = input("Enter : ")

lower(String)
upper(String)
digit(String)

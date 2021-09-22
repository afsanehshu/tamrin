class counter:
     def __init__(self, x=0, y=1):
          self.x = x
          self.y = y
          
     def __str__(self):
          return str(self.x)
     
     def count(self):
          self.x += self.y
          return self.x
          

obj = counter(1,5)

print(obj.__str__())
print(obj.count())

class calc:
     def __init__(self, a, b):
          self.a = a
          self.b = b

     def sum(self):
          return self.a + self.b

     def sub(self):
          return self.a - self.b

     def mul(self):
          return self.a * self.b

     def div(self):
          return self.a / self.b


while True:
     num1 = int(input("Enter First Number: "))
     num2 = int(input("Enter second Number: "))

     print()

     obj = calc(num1,num2)
     print("+ = ",obj.sum())
     print("- = ",-obj.sub())
     print("* = ",obj.mul())
     print("% = ",obj.div())
     print()
     print("--------------------------")
     print()

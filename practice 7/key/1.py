class Time:
     def __init__(self, hour=0, minute=0, secend=0):
          self.hour = hour
          self.minute = minute
          self.secend = secend

     def __str__(self):
          return "{0:02d} : {1:02d} : {2:02d}".format(self.hour, self.minute, self.secend)

     def __add__(self, other):
          if isinstance(other, Time):
               return self.afzoodane_Time(other)
          else:
               return self.afzayesh(other)

     def __radd__(self, other):
          return self.__add__(other)

     def __repr__(self):
        print("{0:02d} : {1:02d} : {2:02d}".format(self.hour, self.minute, self.secend))

     def afzayesh(self, secends):
          secends += self.Time_To_int()
          return self.int_To_Time(secends)

     def afzoodane_Time(self, other):
          secends = self.Time_To_int() + other.Time_To_int()
          return self.int_To_Time(secends)

     def Time_To_int(self):
          minutes = self.hour * 60 + self.minute
          secends = minutes * 60 + self.secend
          return secends

     def int_To_Time(self, secends):
          minutes, self.secend = divmod(secends, 60)
          self.hour, self.minute = divmod(minutes, 60)
          return self
     

T = Time(2,45,12)
T1 = Time(3,5,28)

T.__add__(T1)
T.__repr__()


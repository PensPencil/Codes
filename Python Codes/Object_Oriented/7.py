from math import trunc
class Time:
    def __init__(self,hour=0,min=0):
        self.hour = hour
        self.min = min
        if self.min>60:
            self.hour+=trunc(self.min/60)
            self.min = self.min%60
    def displayTime(self):
        print("The Time is :",self.hour," hour(s) and ",self.min," minute(s).")

    def addTime(obj1,obj2):
        res = Time(0,0)
        res.hour = obj1.hour + obj2.hour
        res.min = obj1.min + obj2.min
        if res.min > 60:
            res.hour+=trunc(res.min/60)
            res.min=res.min%60
        res.displayTime()
    def displayMinutes(self):
        print("There are ",(self.hour*60+self.min)," minutes in ",self.hour," hour(s) and ",self.min," minute(s).")
    
obj1 = Time(3,69)
obj2 = Time(2,3)
obj3 = Time.addTime(obj1,obj2)
obj1.displayTime()
obj2.displayMinutes()



    
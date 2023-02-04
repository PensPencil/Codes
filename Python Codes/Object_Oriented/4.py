class rectangle:
    def __init__(self,length = 0,breadth = 0):
        self.length = length
        self.breadth = breadth
        if self.length != 0 and self.breadth == 0:
            self.breadth = self.length
    def area(self):
        ar = self.length*self.breadth
        return ar

rect1 = rectangle()
print(rect1.area())
rect2 = rectangle(3)
print(rect2.area())
rect3 = rectangle(3,4)
print(rect3.area())
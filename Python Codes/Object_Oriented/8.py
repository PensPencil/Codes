class Triangle:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        self.peri = self.side1+self.side2+self.side3
        print("The perimeter of the triangle is :",self.peri)
    def area(self):
        self.s = self.peri/2
        self.ar = (self.s*(self.s-self.side1)*(self.s-self.side2)*(self.s-self.side3))**0.5
        print("The area of the triangle is :{0:.2f}".format(self.ar))
obj1 = Triangle(3,4,5)
obj1.perimeter()
obj1.area()

obj2 = Triangle(5,6,7)
obj2.perimeter()
obj2.area()
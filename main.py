class Circle():
    def __init__(self , radius):
        self.radius = radius
    def area(self):
       
        print("area is :- " ,3.14 * (self.radius * self.radius))
    def perimeter(self):
        print("perimeter ius :- ",(2 * 3.14) *(self.radius))
c1 = Circle(21)
c1.area()
c1.perimeter()
        
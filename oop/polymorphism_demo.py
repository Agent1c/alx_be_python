import math

class Shape:
    def area(self):
        raise NotImplementedError() #raises a NotImplementedError
    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width #calculate the rectangle’s area using the formula: length × width.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.radius = self.radius** 2 * math.pi #calculate the circle’s area using the formula: π × radius² (use math.pi for π).
        return self.radius
    

# def area_of_the_circle (Radius):   
#     area = Radius** 2 * math.pi  
#     return area  
# Task 2: Shapes & Polymorphism. See ../python.md for the full task.
# Replace this comment with a one-sentence description of your approach.

import math


class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    # TODO: add a __repr__ so printing a shape shows its type and area.


# TODO: class Circle(Shape) storing radius r, overriding area() -> pi * r**2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow (self.radius , 2)
    
    def __repr__(self):
        return f"Circle(area={self.area()})"
    

# TODO: class Rectangle(Shape) storing w, h, overriding area() -> w * h
class Rectangle(Shape):
    def __init__(self , width , hight):
        self.width=width
        self.hight = hight

    def area(self):
        return self.width * self.hight
    
    def __repr__(self):
        return f"Rectangle(area={self.area()})"
        


def main():
    # TODO: make a mixed list (>=2 circles, >=2 rectangles), then use a single
    # loop to print each shape and accumulate the total area; print the total.
    ...
    circle1 = Circle(2)
    circle2 = Circle(7)
    rectnagle1 = Rectangle(10,2)
    rectnagle2 = Rectangle(15,5)

    total_area = 0

    for object in (circle1, circle2, rectnagle1 , rectnagle2):
        print(object.__repr__())
        total_area += object.area()

    print(f"the sum of areas: {total_area}")



if __name__ == "__main__":
    main()

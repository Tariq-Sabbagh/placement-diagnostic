# Task 2: Shapes & Polymorphism. See ../python.md for the full task.
# Replace this comment with a one-sentence description of your approach.

import math


class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    # TODO: add a __repr__ so printing a shape shows its type and area.


# TODO: class Circle(Shape) storing radius r, overriding area() -> pi * r**2
# TODO: class Rectangle(Shape) storing w, h, overriding area() -> w * h


def main():
    # TODO: make a mixed list (>=2 circles, >=2 rectangles), then use a single
    # loop to print each shape and accumulate the total area; print the total.
    ...


if __name__ == "__main__":
    main()

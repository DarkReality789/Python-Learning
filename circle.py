import math


class Circle:
    radius = 5

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        return area

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


circle_1 = Circle(7)
print("This is your area " + str(circle_1.calculate_area()))
print("This is your perimeter " + str(circle_1.calculate_perimeter()))




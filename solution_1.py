class Circle:
    pi = 3.1415
    all_circles = []

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        return self.pi * self.radius ** 2

    @staticmethod
    def total_area():
        total_area = 0
        for circle in Circle.all_circles:
            total_area += circle.area()
        return total_area
    
    def __str__(self):
        return f'{self.radius}'

    def __repr__(self):
        return f'{self.radius}'

    

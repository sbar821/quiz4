class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return 2 * self._radius

    def get_area(self):
        return 3.14159 * self._radius ** 2

    def get_circumference(self):
        return 2 * 3.14159 * self._radius

    def scale_radius(self, scale_factor):
        self._radius *= scale_factor

def main():
    circle = Circle(5)
    print(circle.get_radius())  
    print(circle.get_diameter())  
    print(circle.get_area())  
    print(circle.get_circumference())  
    circle.scale_radius(2)
    print(circle.get_radius())  

if __name__ == "__main__":
    main()
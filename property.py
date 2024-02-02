class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

    def scale_radius(self, scale_factor):
        self._radius *= scale_factor

def main():
    circle = Circle(5)
    print(f"Radius: {circle.radius}")
    print(f"Diameter: {circle.diameter}")
    print(f"Area: {circle.area}")
    print(f"Circumference: {circle.circumference}")

    circle.scale_radius(2)
    print("\nAfter scaling radius by 2:")
    print(f"Radius: {circle.radius}")
    print(f"Diameter: {circle.diameter}")
    print(f"Area: {circle.area}")
    print(f"Circumference: {circle.circumference}")


if __name__ == "__main__":
    main()
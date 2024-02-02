from mod2.radius import calculate_radius
from mod1.diameter import calculate_diameter
from mod3.area import calculate_area

def main():
    radius = calculate_radius(10)
    diameter = calculate_diameter(radius)
    area = calculate_area(radius)

    print(f"The radius of the circle is {radius}.")
    print(f"The diameter of the circle is {diameter}.")
    print(f"The area of the circle is {area}.")

if __name__ == "__main__":
    main()

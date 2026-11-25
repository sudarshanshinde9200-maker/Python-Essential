import math

def calculate_area(shape, *dimensions):

    if shape == "circle":
        radius = dimensions[0]
        return math.pi * radius * radius

    elif shape == "rectangle":
        length, breadth = dimensions
        return length * breadth

    elif shape == "triangle":
        base, height = dimensions
        return 0.5 * base * height

    else:
        return None

shape = input("Enter shape (circle/rectangle/triangle): ").lower()

if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", calculate_area(shape, r))

elif shape == "rectangle":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area:", calculate_area(shape, l, b))

elif shape == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", calculate_area(shape, b, h))

else:
    print("Invalid shape")
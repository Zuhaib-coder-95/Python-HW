import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Enter the radius: "))
result = calculate_circumference(radius)
print(result)
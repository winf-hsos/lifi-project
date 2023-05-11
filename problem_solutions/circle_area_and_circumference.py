import math

# TODO: Get the input (radius) from the user
radius = input("What's the radius of the circle? ")
radius = float(radius)

# TODO: Calculate area and circumference based on the radius
area = math.pi * radius * radius
circumference = math.pi * 2 * radius

# TODO: Print area and circumference to the console
print(f"Area of the circle is {area:.3f}")
print(f"Cirumference of the circle is { circumference:.3f}")
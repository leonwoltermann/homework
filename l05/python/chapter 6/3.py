import math

r = float(input("enter the radius of the sphere: "))

area = 4 * math.pi * r * r

volume = 4.0/3.0 * math.pi * r**3
 
print(f"The surface area is {area} square units.")
print(f"The volume is {volume} cubic units.")


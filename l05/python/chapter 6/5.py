import math

diameter = float(input("Enter diameter of pizza: "))
cost = float(input("Enter price of pizza: "))

area = math.pi * (0.5 * diameter) ** 2

diametercost = cost / area

print(f"The price of the pizza is {diametercost} per square")


 
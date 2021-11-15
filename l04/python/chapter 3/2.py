import math

def main():
    print("This program calculates the price per square inch of a pizza")
    diameter = float(input("Enter the diameter of the pizza in inch: "))
    price = float(input("Enter the price of the pizza in any currency: "))
    currency = input("Enter the name of the currency: ")


    area = math.pi * (diameter / 2) ** 2
    priceArea = area / price
    print("one square inch costs", priceArea, currency)
    
main()

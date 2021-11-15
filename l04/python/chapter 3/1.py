import math

def main():

    print("This program calculates the surfaces area and volume of a sphere ")

    radius = float(input("enter the radius: "))
    volume = 4 / 3 * math.pi * radius ** 2
    surface = 4 * math.pi * radius **2

    print("The volume of the sphere is", volume)
    print("The surface area of the sphere is", surface)
   
main()

import math

def main():
	print("This program calculates the distance between two points")
	x1, y1 = eval(input("Enter the cordinates of the first point: "))
	x2, y2 = eval(input("Enter the cordinates of the second point: "))
	distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	print("The distance is" distance)
main()
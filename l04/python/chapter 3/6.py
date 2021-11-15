def main():
	print("This program calculates the slope of a line between two points")
	x1, y1 = eval(input("Enter the x and y cordinates of the first point with a comma between the values: "))
	x2, y2 = eval(input("Enter the x and y cordinates of the second point: "))
	slope = (y2 - y1) / (x2 - x1)
	print("The slope of the line is", slope)

main()
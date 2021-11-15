def main():
	print("This program calculates the epact of a year")
	year = int(input("Enter the year in four digits: "))

	c = year//100
	epact = (8 + (c//4)- c + ((8 * c + 13)//25) + 11 * (year%19))%30

	print("The epact of", year, "is", epact)
	
main()
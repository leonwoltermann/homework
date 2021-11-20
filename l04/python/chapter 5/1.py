def main():
	dateStr = input("Enter a date (mm/dd/yyyy): ")
	monthStr, dayStr, yearStr = dateStr.split("/")
	months = ["January", "February", "March", "April",
	 "May", "June", "July", "August", 
	 "September", "October", "November", "Dezember"]
	monthStr = months[int(monthStr)-1]
	print("{0} {1}, {2}".format(monthStr, dayStr, yearStr))

main()
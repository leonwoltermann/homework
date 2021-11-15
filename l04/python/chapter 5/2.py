def main():
	print("This program converts a quiz score to a grade")
	score = int(input("Enter score: "))
	grades = ["F", "F", "D", "C", "B", "A"]
	grade = grades[score]
	print(grade)

main()

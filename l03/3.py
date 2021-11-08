def main():
    print("This program prints the average of three exam scores")
    score1, score2, score3 = eval(input("Enter the scores seperated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("the average score is:", average)

main()

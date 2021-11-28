interest = float(input("Enter the interest rate: "))
investment = 1
aim = investment * 2
count = 0

while investment <= aim:
    investment = investment + (investment * interest)
    count += 1

print(f"It takes {count} years the investemnt to double")





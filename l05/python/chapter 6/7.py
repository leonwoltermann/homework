number = int(input("Enter number: "))
x, y = 1,1
for i in range(number-2):
    x, y = x+y, x

print(f"The Fibonacci value is {x}")

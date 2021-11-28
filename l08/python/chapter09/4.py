print("This program prints the Syracuse sequence of any given number")
n = int(input("Enter a number: "))
print(n)
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    elif n % 2 != 0:
        n = (3 * n) + 1
    print(n)

#almost finished
print("This program find every prime smaller than any given number")
n = int(input("Enter a number: "))
for x in range(2, n):
    for y in range(2, n):
        if x % y == 0:
            break
        elif x % y != 0:
            print(f"{x} is a prime")


print("Prime or not?")

for i in range(20): 
    n = int(input("Enter a number: "))

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime")
            break
        elif i == n - 1:
            print(f"{n} is a prime")



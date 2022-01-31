n = int(input("Please enter a natural number: "))

sumN = 0
for i in range(1,n + 1):
    sumN = sumN + i

sum2 = 0
for i in range(1,n + 1):
    sumNcubed = sum2 + i ** 3


print(f"The sum of the first {n} numbers is {sumN}")
print(f"The sum of the cubes of the numbers is {sumNcubed}")



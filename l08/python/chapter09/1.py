def main():
    n = int(input("enter an integer: "))
    x, y = 1, 1
    for i in range(n - 2):
        x, y = x + y, x
    print(x)
main()
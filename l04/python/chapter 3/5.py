def main():
    print("This program calculates the costs of an coffe order")
    weight = float(input("How much pounds of coffe you would like to order?: "))

    costs = weight * 10.50 + weight * 0.86 + 1.50

    print("The costs of this order are", costs, "pound")
    
main()

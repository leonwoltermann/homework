def main():
    
    print("This program calculates the molecular weight of carbohydrate")

    H = 1.00794
    C = 12.0107
    O = 15.9994
    
    inputH = float(input("Enter the number of hydrogen atoms in the molecule: "))
    inputC = float(input("Enter the number of carbon atoms in the molecule: "))
    inputO = float(input("Enter the number of oxygen atoms in the molecule: "))

    weight = inputH * H + inputC * C + inputO * O

    print("The weight of the the molecule is", weight)
    
main()

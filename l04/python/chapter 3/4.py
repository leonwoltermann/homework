def main():
    print("This program calculates the distance of lightning")
    sec = int(input("Enter how many seconds passed between you 'saw' and 'heard' the lighting: "))
    distanceFt = sec * 1100
    distanceMile = distanceFt / 5280

    print("The distance to the lightning is", distanceFt, "feet and", distanceMile, "miles")

main()

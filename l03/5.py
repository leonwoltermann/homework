def main():
    print("Celsius to Fahrenheit Converter")
    print("|Celsius|", "|Fahrenheit|")
    for celsius in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        fahrenheit = 9/5 * celsius + 32
        print("|"  ,f"{celsius :^5d}",   "|", "|  ", f"{fahrenheit :^5}", " |")


main()

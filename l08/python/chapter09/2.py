




def windChillIndex():
    for v in range(0, 60, 5):
        for t in range(-20, 70, 10):
            windChill = 35.74 + (0.62125 * t) - (35.75 * (v ** 0.16)) + ((0.4275 * t) * (v ** 0.16))
            print("|{:^4}|".format(int(windChill)), end = " ")
            if t == 60:
                print("\n")

windChillIndex()

       


    


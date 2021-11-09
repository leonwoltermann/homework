def main():

    #Introduction
    print("Bahasa Indonesia Quiz-----------------------------------------------")
    x = input("to start type 'start': ")
    while x != "start":
        x = input("to start type 'start': ")
    
    #Rules
    print()
    print("Rules---------------------------------------------------------------")    
    print("-For every question you will get 3 attempts")
    print("-Just use lowercase letters for the answers")
    x = input("to continue type 'ok': ")
    while x != "ok":
         x = input("to continue type 'ok': ")

    #trueAnswers and falseAnswers variables
    trueAnswers = 0
    falseAnswers = 0

    #First question
    print()    
    print("First Question------------------------------------------------------")
    print("Is 'kanan' (a) left or (b) right?")
    for i in range(3):
        x = input("type 'a' or 'b' for your answer: ")
        if x == "b":
            trueAnswers = trueAnswers + 1
            print()
            print("Correct-------------------------------------------------------------")
            break 
        else:
            falseAnswers = falseAnswers + 1
            print()
            print("Wrong---------------------------------------------------------------")
            print()
            continue

    #Second question
    print()    
    print("Second Question-----------------------------------------------------")
    print("Which pronoun represents the first person singular")
    print("(a) saya or (b) kamu?")
    for i in range(3):
        x = input("type a or b for your answer: ")
        if x == "a":
            trueAnswers = trueAnswers + 1
            print()
            print("Correct-------------------------------------------------------------")
            break
        else:
            falseAnswers = falseAnswers + 1
            print()
            print("Wrong---------------------------------------------------------------")
            print()
            continue

    #Third question   
    print()
    print("Third Question------------------------------------------------------")
    print("Name a weekday in Bahasa Indonesia.")
    for i in range(3):
        x = input("type to give an answer: ")
        if (x == "senin" or x == "selasa" or x == "rabu" or x == "kamis" or x == "jumat" or x == "sabtu"  or x == "minggu"):
            trueAnswers = trueAnswers + 1
            print()
            print("Correct-------------------------------------------------------------")
            break
        else:
            falseAnswers = falseAnswers + 1
            print()
            print("Wrong---------------------------------------------------------------")
            print()
            print(x, "is not the name of a weekday in Bahasa Indonesia")
            continue

    print("'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', and 'minggu' are the weekdays in Bahasa Indonesia")    

    #Fourth question  
    print()    
    print("Fourth Question-----------------------------------------------------")
    print("Is mingu a weekday in Bahasa Indonesia?")
    for i in range(3):
        x = input("type 'true' or 'false' for your answer: ")
        if x == "false":
            trueAnswers = trueAnswers + 1
            print()
            print("Correct-------------------------------------------------------------")
            break
        else:
            falseAnswers = falseAnswers + 1
            print()
            print("Wrong---------------------------------------------------------------")
            print()
            continue
    
    #End
    print()
    print("Game Over")

    #Print trueAnswers and falseAnswers variables
    print("You gave", trueAnswers, "correct and", falseAnswers, "wrong answers")



main()

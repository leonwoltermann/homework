def oldMac():
    print("Old MacDonald had a farm, Eh-igh, Eh-igh, Oh!")

def animal(animal, sound):
    oldMac()
    print("And on the farm he had a", animal, "Eh-igh, Eh-igh, Oh!")
    print("With a", sound + ",", sound, "here and a", sound + ",", sound, "there.")
    print("Here a", sound, "there a", sound + ", everywhere a", sound + ".")
    print()

def main():
    animal("cow", "moo")
    animal("dog", "woof")
    animal("cat", "meow")
    animal("duck", "quack")
    animal("sheep", "baa")

main()





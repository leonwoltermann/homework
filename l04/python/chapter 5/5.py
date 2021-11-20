#uncomplete but almost finished

def main():
    name = input("Enter your name: ")
    total = 0
    for letter in name:
      total = total + ord(letter.lower()) - ord("a")+1
    print(total)
    





    #letters = list(name)
    alphabet = ["0","a","b", "c","d","e",
                "f","g","h","i","j","k",
                "l","m","n","o","p","q",
                "r","s","t","u","v","w",
                "x","y","z"]

    #letters_as_set = set(letters)
    #intersection = letters_as_set.intersection(alphabet)
    #print(intersection)

    #for i in letters:
      #  values = alphabet.index(i)
       # print(values)

    


   # listValues = list(map(int, values))
    #print(listValues)

   # output = sum(values)
    
   # print(output)


    #[alphabet.index(x) for x in letters]
       # print(x)
    

    #position = letters.index(alphabet)
    #print(position)
    
    #for i in letters:
      #  position = letters.index()
        #print(position)
        

main()
        

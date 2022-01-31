def main():
    inputphrase = input("Enter a phrase: ").upper()
    phrase = inputphrase.split(" ")
    acronym = ""
    for i in phrase:
        acronym = acronym + i[0]
    print(f"The acronym from {inputphrase} is {acronym}")
        
main()


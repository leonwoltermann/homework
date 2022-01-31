
decipherkey = int(input("Enter the key: "))
phrase = input("Enter text: ")
decodedtext = ""
for letter in phrase:
    cipher = cipher + chr(ord(letter) + decipherkey)


print(f"the encoded text is {cipher}")


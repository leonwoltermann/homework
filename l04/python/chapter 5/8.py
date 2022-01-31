
decipherkey = int(input("Enter the key: "))
phrase = input("Enter text: ")

characters = "abcdefghijklmnopqrstuvwxyz"

cipher = ""
for letter in phrase:
    position = characters.find(letter)
    newposition = (position + decipherkey) % len(characters)
    cipher = cipher + characters[newposition]

print(f"the encoded text is {cipher}")


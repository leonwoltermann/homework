name = input("Enter a name: ")

letters = "".join(name.split())
total = 0
for letter in letters:
    total = total + ord(letter.lower()) - ord('a') + 1

print(f"The value of {name.upper()} is:", total)
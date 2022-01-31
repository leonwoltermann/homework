def byFreq(pair):
    return pair[1]

#opens file
text = open("tangosadimin_Clean.md", "r").read()
#converts all characters in lowercase
text = text.lower()
#iterates through all character
for ch in "#$%&\"'()*+,-./:;<=>?@[\\]^_`{|}~":
    #replaces them by space
    text = text.replace(ch, " ")
#split text into words
words = text.split()

#creates dict for word counts
counts = {}
#iterates through all words
for w in words:
    #creates an entry into the counts dict and adds a 1 to the count
    counts[w] = counts.get(w, 0) + 1

#returns dict as a list
items = list(counts.items())
#sorts the list by frequence but reverse so the highest frequence words are at the begining
items.sort(key=byFreq, reverse=True)


for i in range(1):
    word, count = items[i]

print(items[100:200])
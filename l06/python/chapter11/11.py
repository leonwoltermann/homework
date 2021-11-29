def byFreq(pair):
    return pair[1]

text = open(r"/Users/leonwoltermann/Documents/Git/homework/l08/python/chapter11/SitiNurbaya.txt", "r").read()
text = text.lower()
for ch in "#$%&\"'()*+,-./:;<=>?@[\\]^_`{|}~":
    text = text.replace(ch, " ")
words = text.split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

items = list(counts.items())
items.sort()
items.sort(key=byFreq, reverse=True)
for i in range(1):
    word, count = items[i]
    print(word, count)



    
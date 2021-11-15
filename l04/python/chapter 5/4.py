def main():
	phrase = input("Enter a phrase: ").title()
	phrase = phrase.split(" ")
	word1, word2, word3 = phrase[0], phrase[1], phrase[2]
	acronym = word1[0] + word2[0] + word3[0]
	print(acronym)
main()
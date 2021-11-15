from re import search

notAllowed = '[gkmqvwxzios]'

words = open('words.txt', 'r').readlines()

longestWords = ['']

for word in words:
	word = word.strip()
	if search(notAllowed, word) == None:
		if len(word) > len(longestWords[0]):
			longestWords = [word]
		elif len(word) == len(longestWords[0]):
			longestWords.append(word)

print(*longestWords, sep = '\n')
input('Press Enter to exit')
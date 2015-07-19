import nltk
import random
import sys

adjs = ['so', 'such', 'very', 'much', 'many', 'how']
emots = ['wow', 'amaze', 'excite']

def superdogeify(text):
	print " "
	textArray = text.split()
	nouns = []
	resultArray = []
	for word in textArray:
		if word.lower() in adjs:
			continue
		tagSymbol = nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1]
		if tagSymbol == "N" or tagSymbol == "J":
			nouns.append(word)
	lastAdj = ""
	lastAdj2 = ""
	for word in nouns:
		randNum = random.randint(1,100)
		if randNum <= 5 and lastAdj != "so" and lastAdj2 != "so":
			resultArray.append("so wow.")
		elif randNum <= 10:
			resultArray.append("wow.")
		tempAdjs = list(adjs)
		if lastAdj in adjs: tempAdjs.remove(lastAdj)
		if lastAdj2 in adjs: tempAdjs.remove(lastAdj2)
		randomAdj = random.choice(tempAdjs)
		lastAdj2 = lastAdj
		lastAdj = randomAdj
		if randNum <= 10:
			randomAdj.capitalize()
		resultArray.append(randomAdj + ( " " + word.lower().rstrip('?:!.,;') + "."))
	index = 0
	for originalWord in resultArray:
		word = originalWord
		word = word.replace('dog', 'doge')
		word = word.replace('dogee', 'doge')
		word = word.replace('please', 'plz')
		word = word.replace('really', 'rly')
		word = word.replace('cat', 'cate')
		resultArray[index] = word
		index += 1
	
	# Catch-all clause: if result is empty, just return "Wow."
	if len(resultArray) == 0 :
		resultArray.append("wow")
	return resultArray


def main():
	userString = raw_input("Enter text:")
	result = superdogeify(userString)
	print "" # so newline
	print result


if __name__ == "__main__":
	main()



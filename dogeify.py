import nltk
import random
import sys

adjs = ['so', 'such', 'very', 'much', 'many', 'how']
emots = ['wow', 'amaze', 'excite']

def superdogeify(text):
	print " "
	textArray = text.lower().split()
	nouns = []
	resultArray = []
	for word in textArray:
		if word.lower() in adjs:
			continue
		tagSymbol = nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1]
		if tagSymbol == "N" or tagSymbol == "J":
			#if tagSymbol == "N":
			nouns.append(word)
	lastAdj = ""
	lastAdj2 = ""
	for word in nouns:
		randNum = random.randint(1,100)
		if randNum <= 5 and lastAdj != "so" and lastAdj2 != "so":
			resultArray.append("So wow.")
		elif randNum <= 10:
			resultArray.append("Wow.")
		tempAdjs = list(adjs)
		if lastAdj in adjs: tempAdjs.remove(lastAdj)
		if lastAdj2 in adjs: tempAdjs.remove(lastAdj2)
		randomAdj = random.choice(tempAdjs)
		lastAdj2 = lastAdj
		lastAdj = randomAdj
		if randNum <= 30:
			resultArray.append(randomAdj.capitalize() + ( " " + word.rstrip('?:!.,;') + "."))
		else:
			resultArray.append(randomAdj + ( " " + word.rstrip('?:!.,;') + "."))
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
		resultArray.append("Wow.")
	return resultArray


def main():
	userString = raw_input("Enter text:")
	result = superdogeify(userString)
	print "" # so newline
	print result


if __name__ == "__main__":
	main()



import nltk
import random
import sys
import re
from colors import *

adjs = ['so', 'such', 'very', 'much', 'many', 'how']
emots = ['wow', 'amaze', 'excite']

# Always strip away double-quotes, smart double-quotes, em-dashes (--)
# and ellipses (...)
stripPattern=ur'["\u201c\u201d\u2014\u2026]'
lstripPattern='-'
rstripPattern=u'?:!.,;'

# replace unicode chars that would otherwise confuse nltk (i.e. smart quotes)
def scrubunicode(text):
	# simplify smart single-quotes
	text = text.replace(u'\u2018', "'").replace(u'\u2019', "'")
	return re.sub(stripPattern, "", text)

def dogeify(text):	
	text = scrubunicode(text)
	textArray = text.split()
	nouns = []
	resultArray = []
	for word in textArray:
		if word.lower() in adjs:
			continue
		# strip away unwanted characters
		word = word.lstrip(lstripPattern).rstrip(rstripPattern)

		# If the entire word was scrubbed away, don't pass it to NLTK!
		if len(word) < 1:
			continue
		
		tagSymbol = nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1]
		if tagSymbol == "N" or tagSymbol == "J":
			nouns.append(word)
	lastAdj = ""
	lastAdj2 = ""
	lastEmot = ""
	for word in nouns:
		randNum = random.randint(1,100)
		if randNum <= 5 and lastAdj != "so" and lastAdj2 != "so":
			tempEmots = list(emots)
			if lastEmot in emots: tempEmots.remove(lastEmot)
			randomEmot = random.choice(tempEmots)
			lastEmot = randomEmot
			resultArray.append("so " + randomEmot + ".")
		randNum = random.randint(1,100)
		if randNum <= 10:
			resultArray.append("wow.")
		tempAdjs = list(adjs)
		if lastAdj in adjs: tempAdjs.remove(lastAdj)
		if lastAdj2 in adjs: tempAdjs.remove(lastAdj2)
		randomAdj = random.choice(tempAdjs)
		lastAdj2 = lastAdj
		lastAdj = randomAdj
		randNum = random.randint(1,100)
		if randNum <= 10:
			randomAdj = randomAdj.capitalize()
		resultArray.append(randomAdj + ( " " + word.lower() + "."))
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

def colorify(dogeArray):
	coloredArray = []
	for dogePair in dogeArray:
		coloredArray.append([dogePair, random.choice(htmlColors.keys())])
	return coloredArray






def main():
	userString = raw_input("Enter text:")
	result = dogeify(userString)
	print "" # so newline, many comment # such inception # wow?
	print result


if __name__ == "__main__":
	main()



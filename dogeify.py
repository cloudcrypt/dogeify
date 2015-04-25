import nltk
import random
import sys
from tqdm import *

adjs = ['so', 'such', 'very', 'much', 'many', 'how']
emots = ['wow', 'amaze', 'excite']

sentence = "The brown fox jumped over the lazy dog. The test, the sentence."



def dogeify(text):
	print " "
	textArray = text.split()
	resultArray = []
	index = 0 
	for word in tqdm(textArray):
		#progress = int(((index + 1) / float(len(textArray))) * 100)
		#sys.stdout.write("\r%d%% Complete..." % progress)
		if word.lower() == "the":
			if index == 0 or index > 0 and textArray[index-1][len(textArray[index-1])-1] == ".":
				resultArray.append("Very")
			else:
				randNum = random.randint(1,2)
				if randNum == 1:
					resultArray.append("such")
				elif randNum == 2:
					resultArray.append("so")
				#resultArray.append("such")
		else:
			if nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1] == "N":
				print word
			if nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1] == "V":
				randNum = random.randint(1,2)
				if randNum == 1:
					#resultArray.append("much")
					resultArray.append(random.choice(adjs))
					resultArray.append(word)
				elif randNum == 2:
					#resultArray.append("many")
					resultArray.append(random.choice(adjs))
					resultArray.append(word)
			else:
				resultArray.append(word)
		index += 1
	return " ".join(resultArray)
	
def superdogeify(text):
	print " "
	textArray = text.split()
	nouns = []
	resultArray = []
	for word in tqdm(textArray):
		if nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1] == "N":
			nouns.append(word)
	for word in nouns:
		randNum = random.randint(1,100)
		if randNum <= 10:
			resultArray.append("So wow.")
		elif randNum <= 20:
			resultArray.append("Wow.")
		resultArray.append(random.choice(adjs).capitalize())
		resultArray.append((word + "."))

	return " ".join(resultArray)
	
	
	
	
	
def main():
	userString = raw_input("Enter text:")
	result = superdogeify(userString)
	print ""
	print result


if __name__ == "__main__":
	main()



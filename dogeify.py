import nltk
import random
import sys

adjs = ['so', 'such', 'very', 'much', 'many', 'how']
emots = ['wow', 'amaze', 'excite']

sentence = "The brown fox jumped over the lazy dog. The test, the sentence."



def dogeify(text):
	print " "
	textArray = text.split()
	resultArray = []
	index = 0 
	for word in textArray:
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
	for word in textArray:
		tagSymbol = nltk.pos_tag(nltk.word_tokenize(word))[0][1][:1]
		#if tagSymbol == "N" or tagSymbol == "J":
		if tagSymbol == "N":
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
		resultArray.append(randomAdj.capitalize() + ( " " + word.rstrip('?:!.,;') + "."))
		#resultArray.append((word.rstrip('?:!.,;') + "."))
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
	#return " ".join(resultArray)
	
	
	
	
	
def main():
	userString = raw_input("Enter text:")
	#userString = """
# 	Two households, both alike in dignity,
# In fair Verona, where we lay our scene,
# From ancient grudge break to new mutiny,
# Where civil blood makes civil hands unclean.
# From forth the fatal loins of these two foes
# A pair of star-cross'd lovers take their life;
# Whose misadventured piteous overthrows
# Do with their death bury their parents' strife.
# The fearful passage of their death-mark'd love,
# And the continuance of their parents' rage,
# Which, but their children's end, nought could remove,
# Is now the two hours' traffic of our stage;
# The which if you with patient ears attend,
# What here shall miss, our toil shall strive to mend.
# """
	result = superdogeify(userString)
	print ""
	print result


if __name__ == "__main__":
	main()



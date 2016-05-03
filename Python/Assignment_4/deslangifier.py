#!/usr/bin/env	python3
#Austin Metzner
#Melissa Bica
#Assignment 4
counter = 0
#"textToEnglish2014.csv"

def CreateDictionary(filetoopen):
	fo = open(filetoopen, "r")
	#Dict = list()
	#fo.readlines
	Dictionary = {} #Sets up dictionary
	for line in fo:
		#Makes list split by commas
		Dict = line.split(",")
		#Both dictionaries equal each other
		string = Dict[1]
		Dictionary[Dict[0]] = string.rstrip("\n")

		#Prints dictionary
		print(Dict[0])
		#print(Dict[1])

	return Dictionary
	fo.close()


def main():
	wordDictionary = CreateDictionary("textToEnglish2014.csv")
	#print (wordDictionary)
	print(" ")
	print("Which text abbreviations would you")

	#Get the user input
	userInput = input("like to have translated (separated by space): ")
	splitInput = userInput.split(" ") #When in the for loop did not work
	translations = ""
	for line in splitInput: # each 'item' in userin is split into separate items
		if line in wordDictionary:
			#print(wordDictionary[line])
			translations += (wordDictionary[line]) + (" ")
		else:
			print("NF")
			translations += ("NF ")

	print (translations)

	#Loop until user inputs q
	quitt = input("Enter q to quit: ")
	while quitt != "q":
		main()


main()

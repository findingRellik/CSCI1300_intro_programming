#Project 1: Tic Tac Toe incorporating a Twitter API
#Austin Metzner

import sys #for the sys.exit functionality
import time #Because twitter API isn't blazing fast and because user input could happen before API fetch was done and it gives user time to read encouraging quote
#These are the rules for the user to read, not contained in main for obvious reasons #I could make it a function but nah
print ("Welcome to INSPIRATIONAL Tic Tac Toe!")
print " " #Python 2.7 TROLOLOLOL
print ("User 1 goes first")
print (" ")
print ("Here is how you play this version of Tic Tac Toe:")
print (" ")
print ("Imagine a Tic Tac Toe grid. Starting in the top left corner")
print ("the grid is assigned the number 1, and the one directly to the")
print ("right is assigned number 2. So the bottom right of the grid")
print ("would be number 9. To select where you want to go, select a")
print ("number between 1 and 9 accordingly when it is your turn.")
print (" ")
print "Also, wait a solid 4 seconds for your encouragement to show"
print ("Good luck! May the better man win.")
print (" ")

line0 = ("   |   |   ")
line1 = ("_1_|_2_|_3_")
line2 = ("_4_|_5_|_6_")
line3 = ("_7_|_8_|_9_")
line4 = ("   |   |   ")

def drawBoard(): #Created this for the sole purpose of when you restart the game
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
#drawBoard()

#These determine whether a player wins through the didIwin function
userMoves = []
user1ins = []
user2ins = []

#This is to incorporate a twitter API in my program
import random
import twitter
consumer_key='FMDM33d8bSm1N4P0VC0QtqYz5'
consumer_secret='f4uojz7IW8Qjvnu7HF6pqAS5tlvCE7JTbLoH2o8OeswSzPSLeq'
access_token='832507950-vGlaT3wSpob7k8GkX3n6MI8XCASiIb6F0HCxNa4S'
access_token_secret='A33B6OhZ900NBXU4ymeXMvPbYki11pEUUcdNRj6ceuP8z'
api = twitter.Api(consumer_key, consumer_secret,access_token,access_token_secret)#line2205 #gives me access to the twitter database of databases of data
#special = twitter.Status() #Attempt to get favorite count and retweet count from Status class
#print api.VerifyCredentials() #works #Used it to check if my access token worked

def replaceNumber1(var,line0, line1, line2, line3,line4): #This is how user 1 makes a move, player 2 has the same function but with O's
	global userMoves
	global user1ins
	var = moveValid(var) #checks if move is a number 1-9
	var = isSpotTaken(var) #Makes sure the valid move is not a move that has already been made
	if var  == "1":
		line1 = line1.replace("1","X") #swaps out the number the user chose for an x
	elif var == "2":
		line1 = line1.replace("2","X")
	elif var == "3":
		line1 = line1.replace("3","X")
	elif var == "4":
		line2 = line2.replace("4","X")
	elif var == "5":
		line2 = line2.replace("5","X")
	elif var == "6":
		line2 = line2.replace("6","X")
	elif var == "7":
		line3 = line3.replace("7","X")
	elif var == "8":
		line3 = line3.replace("8","X")	
	elif var == "9":
		line3 = line3.replace("9","X")
	else: 
		print("Error")
		print "Really? Come on man"	
		print "You broke the program" # LOL
	user1ins.append(var) #Updates the list of user inputs for didIwin
	userMoves.append(var) #Updates the list for the purpose of isSpotTaken
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
	return(line0, line1, line2, line3,line4) #This makes sure that the playing board is updated

def replaceNumber2(var, line0, line1, line2, line3, line4): #Same as replaceNumber1 except replaces numbers with O's
	global userMoves
	global user1ins
	var = moveValid(var)
	var = isSpotTaken(var)
	if var  == "1":
		line1 = line1.replace("1","O")
	elif var == "2":
		line1 = line1.replace("2","O")
	elif var == "3":
		line1 = line1.replace("3","O")
	elif var == "4":
		line2 = line2.replace("4","O")
	elif var == "5":
		line2 = line2.replace("5","O")
	elif var == "6":
		line2 = line2.replace("6","O")
	elif var == "7":
		line3 = line3.replace("7","O")
	elif var == "8":
		line3 = line3.replace("8","O")	
	elif var == "9":
		line3 = line3.replace("9","O")
	else: 
		print("Error")
		print "Really? Come on man"
		print "You broke the program"
	user2ins.append(var)
	userMoves.append(var)
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
	return(line0, line1, line2, line3,line4)

#This is my use of the Twitter API to encourage the players of my game
#Api class is on line 2205 in twitter.py and has all the useful functions, control+F allows you to search this schtuff up
encouragingTweets = []
numFavorites = 0
reTweets = 0 #line 523
def getTweet(): #This gets encouraging tweets
	counter = 0
	statuses = api.GetUserTimeline(screen_name ='EncouragedOne', count = 200)#line 2694-2743 #count is number of tweets being imported, screenname is twitter user
	for status in statuses:
		noStuff = ["RT","@","Lord","God","GOD","pray","prayer"]
		if noStuff[0] not in str(status) and noStuff[1] not in str(status) and noStuff[2] not in str(status) and noStuff[3] not in str(status) and noStuff[4] not in str(status) and noStuff[5] not in str(status) and noStuff[6] not in str(status):#I don't what retweets or tweets containing Lord and God not geared towards encouragement of all religious backgrounds
			statuss = status.text #Puts status into text form
			encouragingTweets.append(statuss) #adds select statuses to a list that will be called in printTweet
			counter+=1
			#numFavorites = special.GetFavoriteCount() #Line 250 of twitter.py
			#reTweets = special.GetRetweetCount()
			#numFavorites = status.favorite_count #Line 250 of twitter.py
			#reTweets = status.retweet_count #Neither of these are serving their purpose apparently I'm not using them right	
	return encouragingTweets,counter#, numFavorites, reTweets
	
def printTweet(): #Prints encouraging tweet to encourage player by randomly selecting a number to print a random tweet in list
	encouragingTweets,counter = getTweet()
	lengthOfList = len(encouragingTweets) #Adds 20 tweets to encouragingTweets
	#print lengthOfList #To see how many tweets of the 100 imported aren't retweets or written to specific people
	randNum = random.randint(0,counter)#I got the range from the line above # apparently randrange is faster than rand int
	theTweet = encouragingTweets[randNum] #This will select a random "approved" tweet to display
			#Didn't spend the time to make sure that there were no repeat tweets just that 1/46 would have repeats
	numFavorites = random.randint(80,200)
	reTweets = random.randint(30,90)
	print theTweet
	print " "
	print "Favorited by ", numFavorites,"people | Retweeted ", reTweets," times"
	print " "
	
#These next two functions check if either of the users have won 
def didIwin(list1, user): #list 1 is gonna be the user's input list, isn't called until after the third user input
	userInsSet = set(list1) #sets don't have to be ordered
	winCombos = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
		#winCombos is a set of all the possible win combinations
	for item in winCombos: #This loop makes it easier to go through and check if there are any win matches 
		didTheyWin = userInsSet.issuperset(item) #Checks to see if userins is super set to any win combos, returns True or False
		if didTheyWin is True:
			print "Player ", user," WINS!"
			playAgain = raw_input("PLAY AGAIN? (enter 'q' to quit): ")
			if playAgain != "q":
				main()
			else:
				print " "
				sys.exit("Thanks for playing!")
				
def didIwinFinal(list1): #Did as separate definition for the sole purpose of saying "DRAW" 
	userInsSet = set(list1)
	winCombos = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
	for item in winCombos:
		didTheyWin = userInsSet.issuperset(item) #Checks to see if userins is super set to any win combos
		if didTheyWin is True:
			print "Player 2 WINS!"
			playAgain = raw_input("PLAY AGAIN? (enter 'q' to quit): ")
			if playAgain != "q":
				main()
	print "DRAW!"

def isSpotTaken(var): #checks to see if input hasn't already been used #this works again now
	while var in userMoves:
		print "Try another space: "
		var = raw_input() #str(input()) DOES NOT WORK IN 2.7
	return var
		
def moveValid(var): #Checks to see if input is even a number
	while var not in "1 2 3 4 5 6 7 8 9".split(): # worked with python 3?
		print("Try another space: ")
		var = raw_input() #for some reason this needs to be a string
	return var
	
def eraseLists():	#Trying to figure out how to reset lists after calling main() again
	global userMoves
	userMoves = []
	global user1ins
	user1ins = []
	global user2ins
	user2ins = []
	#return userMoves, user1ins, user2ins
	#Because userMoves and ins are global variables, the lists cannot reset. Maybe try BOOLEAN LOGIC??
	
def main():
	line0 = ("   |   |   ")
	line1 = ("_1_|_2_|_3_")
	line2 = ("_4_|_5_|_6_")
	line3 = ("_7_|_8_|_9_")
	line4 = ("   |   |   ")
	drawBoard()
	
	global userMoves
	global user1ins
	global user2ins
	#userMoves, user1ins, user2ins =
	eraseLists()#I was hoping this would work for when the player chooses to play again
				#Because for some reason whenever the player opts to play again the list of UserMoves isn't cleared
				#This currently screws up the didIwin function
		
	user1in1 = raw_input("User 1 select your move: ") #Had to change it to raw_input since it's 2.7
	line0, line1, line2, line3,line4 = replaceNumber1(user1in1, line0, line1, line2, line3,line4) #This updates the board after the user's input which is then used in the next replaceNumber

	user2in1 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in1, line0, line1, line2, line3,line4)
	
	printTweet()
	time.sleep(1)
	user1in2 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in2, line0, line1, line2, line3,line4)
	
	printTweet()
	time.sleep(1)
	user2in2 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in2, line0, line1, line2, line3,line4)

	printTweet()
	time.sleep(1)
	user1in3 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in3, line0, line1, line2, line3,line4)
	didIwin(user1ins,1) #This is called now because it's the first time a win is possibility

	printTweet()
	time.sleep(1)
	user2in3 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in3, line0, line1, line2, line3,line4)
	didIwin(user2ins,2)
	
	printTweet()
	time.sleep(1)
	user1in4 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in4, line0, line1, line2, line3,line4)
	didIwin(user1ins,1)
	
	printTweet()
	time.sleep(1)
	user2in4 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in4, line0, line1, line2, line3,line4)
	didIwin(user2ins,2)
	
	printTweet()
	time.sleep(1)
	user1in5 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in5, line0, line1, line2, line3,line4)
	didIwinFinal(user1ins)
	
	#The loop that forces the user to hit q in order for the game to quit
	playAgain = raw_input("PLAY AGAIN? (enter 'q' to quit): ")
	if playAgain != "q":
		main()
	else:
		sys.exit("Thanks for playing!")

#getTweet()		
#printTweet() #To check if my use of the API works
main()

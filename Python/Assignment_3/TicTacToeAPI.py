#Project 1: Tic Tac Toe incorporating a Twitter API
#Austin Metzner

import sys
print ("Welcome to Tic Tac Toe!")
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
print ("Good luck! May the better man win.")
print (" ")

line0 = ("   |   |   ")
line1 = ("_1_|_2_|_3_")
line2 = ("_4_|_5_|_6_")
line3 = ("_7_|_8_|_9_")
line4 = ("   |   |   ")
print (line0)
print (line1)
print (line2)
print (line3)
print (line4)

userMoves = []
user1ins = []
user2ins = []

def replaceNumber1(var,line0, line1, line2, line3,line4):
	var = moveValid(var)
	var = isSpotTaken(var)
	#a = moveValid(var)
	#print "heres the gap"
	#b = isSpotTaken(a)
	#print "through both functions"
	#var = b
	#print var

	if var  == "1":
		line1 = line1.replace("1","X")
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
	user1ins.append(var)
	userMoves.append(var)
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
	return(line0, line1, line2, line3,line4)

def replaceNumber2(var, line0, line1, line2, line3, line4):
	var = moveValid(var)
	var = isSpotTaken(var)
	#a = moveValid(var)
	#print "heres the gap"
	#b = isSpotTaken(a)
	#print "through both functions"
	#var = b
	#print var

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
	user2ins.append(var)
	userMoves.append(var)
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
	return(line0, line1, line2, line3,line4)

#possible win combinations
'''
d = "123"
e = "456"
f = "789"
g = "147"
h = "258"
i = "369"
j = "159"
k = "357"
'''

def getTweet():


def didIwin():
	#userMoveSet = set(userMoves)
	#user1set = set(user1ins)
	a = ''.join(user1ins)
	b = ''.join(user2ins)
	c = ''.join(userMoves)
	'''
	d = "123"
	e = "456"
	f = "789"
	g = "147"
	h = "258"
	i = "369"
	j = "159"
	k = "357"
	'''
	d = "123"
	e = "456"
	f = "789"
	g = "147"
	h = "258"
	i = "369"
	j = "159"
	k = "357"
	if d in a:
		sys.exit("Player 1 WINS!")
	elif e in a:
		sys.exit("Player 1 WINS!")
	elif f in a:
		sys.exit("Player 1 WINS!")
	elif g in a:
		sys.exit("Player 1 WINS!")
	elif h in a:
		sys.exit("Player 1 WINS!")
	elif i in a:
		sys.exit("Player 1 WINS!")
	elif j in a:
		sys.exit("Player 1 WINS!")
	elif k in a:
		sys.exit("Player 1 WINS!")
	else:
		print a
		print "Player 1 has not won"

	#user2set = set(user2ins)
	#if user2set == userMoveSet:
		#sys.exit("Player 2 WINS!")
	if b in d:
		sys.exit("Player 2 WINS!")
	elif b in e:
		sys.exit("Player 2 WINS!")
	elif b in f:
		sys.exit("Player 2 WINS!")
	elif b in g:
		sys.exit("Player 2 WINS!")
	elif b in h:
		sys.exit("Player 2 WINS!")
	elif b in i:
		sys.exit("Player 2 WINS!")
	elif b in j:
		sys.exit("Player 2 WINS!")
	elif b in k:
		sys.exit("Player 2 WINS!")
	else:
		print b
		print "Player 2 has not won"

def isSpotTaken(var): #this works again now #tuesday night
	while var in userMoves:
		print "Try another space: "
		var = raw_input() #str(input())
	return var

def moveValid(var):
	digits = ['1','2','3','4','5','6','7','8','9',]
	while var not in "1 2 3 4 5 6 7 8 9".split(): # worked with python 3?
		print("Try another space: ")
		var = raw_input() #for some reason this needs to be a string
	return var

def main():
	line0 = ("   |   |   ")
	line1 = ("_1_|_2_|_3_")
	line2 = ("_4_|_5_|_6_")
	line3 = ("_7_|_8_|_9_")
	line4 = ("   |   |   ")
	user1in1 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in1, line0, line1, line2, line3,line4)

	user2in1 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in1, line0, line1, line2, line3,line4)

	user1in2 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in2, line0, line1, line2, line3,line4)

	user2in2 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in2, line0, line1, line2, line3,line4)

	user1in3 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in3, line0, line1, line2, line3,line4)
	didIwin()

	user2in3 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in3, line0, line1, line2, line3,line4)
	didIwin()

	user1in4 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in4, line0, line1, line2, line3,line4)
	didIwin()

	user2in4 = raw_input("User 2 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber2(user2in4, line0, line1, line2, line3,line4)
	didIwin()

	user1in5 = raw_input("User 1 select your move: ")
	line0, line1, line2, line3,line4 = replaceNumber1(user1in5, line0, line1, line2, line3,line4)
	didIwin()


main()

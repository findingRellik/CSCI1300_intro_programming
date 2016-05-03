#Assignment 3: Tic Tac Toe
#Austin Metzner

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

#def didIwin():
#	if user 

def replaceNumber1(var,line0, line1, line2, line3,line4):
	var = moveValid(var)
	var = isSpotTaken(var)
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
	user2ins.append(var) #I was going to use this to determine winner
	userMoves.append(var)
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)
	return(line0, line1, line2, line3,line4) #allows the board to be updated each time

def isSpotTaken(var):
	while var in userMoves:
		print("Try another space: ")
		var = input()
	return (var)
		
def moveValid(var):
	while var not in "1 2 3 4 5 6 7 8 9".split(): #makes a list
		print("Try another space: ")
		var = input()
	return (var)

def main():
	line0 = ("   |   |   ")
	line1 = ("_1_|_2_|_3_")
	line2 = ("_4_|_5_|_6_")
	line3 = ("_7_|_8_|_9_")
	line4 = ("   |   |   ")
	user1in1 = str(input("User 1 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber1(user1in1, line0, line1, line2, line3,line4)
#line0, line1, line2, line3,line4 = replaceNumber1(user1in1, line0, line1, line2, line3,line4)
#Updates board each time
	user2in1 = str(input("User 2 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber2(user2in1, line0, line1, line2, line3,line4)

	user1in2 = str(input("User 1 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber1(user1in2, line0, line1, line2, line3,line4)

	user2in2 = str(input("User 2 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber2(user2in2, line0, line1, line2, line3,line4)

	user1in3 = str(input("User 1 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber1(user1in3, line0, line1, line2, line3,line4)

	user2in3 = str(input("User 2 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber2(user2in3, line0, line1, line2, line3,line4)

	user1in4 = str(input("User 1 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber1(user1in4, line0, line1, line2, line3,line4)

	user2in4 = str(input("User 2 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber2(user2in4, line0, line1, line2, line3,line4)

	user1in5 = str(input("User 1 select your move: "))
	line0, line1, line2, line3,line4 = replaceNumber1(user1in5, line0, line1, line2, line3,line4)

main()
print("Who won?")

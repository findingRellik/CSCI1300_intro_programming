#Assignment 3: Tic Tac Toe
#Austin Metzner

print ("Welcome to Tic Tac Toe!")
print ("User 1 goes first")
#user1 = input("Enter User 1 name: ")
#user2 = input("Enter User 2 name: ")
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

def showBoard():

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

#user1in1 = str(input("User 1 select your move: "))
#user1in1 is user input 1
#user2in1 = input(" select your move: ")
#userin = 0

line0 = ("   |   |   ")
line15 = ("_1_|_2_|_3_")
line25 = ("_4_|_5_|_6_")
line35 = ("_7_|_8_|_9_")
line4 = ("   |   |   ")

def replaceNumber1(var):
	line0 = ("   |   |   ")
	line1 = ("_1_|_2_|_3_")
	line2 = ("_4_|_5_|_6_")
	line3 = ("_7_|_8_|_9_")
	line4 = ("   |   |   ")

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
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)

def replaceNumber2(var):
	line0 = ("   |   |   ")
	line1 = ("_1_|_2_|_3_")
	line2 = ("_4_|_5_|_6_")
	line3 = ("_7_|_8_|_9_")
	line4 = ("   |   |   ")

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
	print (line0)
	print (line1)
	print (line2)
	print (line3)
	print (line4)

user1in1 = str(input("User 1 select your move: "))
replaceNumber1(user1in1)

user2in1 = str(input("User 2 select your move: "))
replaceNumber2(user2in1)

user1in2 = str(input("User 1 select your move: "))
replaceNumber1(user1in2)

user2in2 = str(input("User 2 select your move: "))
replaceNumber2(user2in2)

user1in3 = str(input("User 1 select your move: "))
replaceNumber1(user1in3)

user2in3 = str(input("User 2 select your move: "))
replaceNumber2(user2in3)

user1in4 = str(input("User 1 select your move: "))
replaceNumber1(user1in4)

user2in4 = str(input("User 2 select your move: "))
replaceNumber2(user2in4)

user1in5 = str(input("User 1 select your move: "))
replaceNumber1(user1in5)

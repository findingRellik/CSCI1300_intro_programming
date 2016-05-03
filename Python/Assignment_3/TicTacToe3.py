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
print ("   |   |   ")
print ("_1_|_2_|_3_")
print ("_4_|_5_|_6_")
print ("_7_|_8_|_9_")
print ("   |   |   ")
'''
sqr1 = "1"
sqr2 = "2"
sqr3 = "3"
sqr4 = "4"
sqr5 = "5"
sqr6 = "6"
sqr7 = "7"
sqr8 = "8"
sqr9 = "9"
'''
def showBoard(sqr):
	print ("   |   |   ")
	print ("_",sqr[1],"_|_",sqr[2],"_|_",sqr[3],"_")
	print ("_",sqr[4],"_|_",sqr[5],"_|_",sqr[6],"_")
	print ("_",sqr[7],"_|_",sqr[8],"_|_",sqr[9],"_")
	print ("     |     |   ")

board = ([' '] * 10)
showBoard(board)
def freeSpace(sqr, move):
	return sqr[move] == ' '

def replace(sqr):
	if user1in1 == "1":
		sqr[1] = "X"
	if user1in1 == "2":
		line1 = line1.replace("2","X")
	if user1in1 == "3":
		line1 = line1.replace("3","X")
	if user1in1 == "4":
		line2 = line2.replace("4","X")
	if user1in1 == "5":
		line2 = line2.replace("5","X")
	if user1in1 == "6":
		line2 = line2.replace("6","X")
	if user1in1 == "7":
		line3 = line3.replace("7","X")
	if user1in1 == "8":
		line3 = line3.replace("8","X")
	if user1in1 == "9":
		line3 = line3.replace("9","X")
	showBoard(Board)
count = 1
while(count < 10):
	# (count-1)%2 gives 0 or 1, add 1 to get the player number
	user1in1 = input("Enter your move player " + str((count-1)%2+1) + ": ")
	if int(user1in1) <= 9 & int(user1in1) >= 1:
		move = int(user1in1)
		if freeSpace(board,move):
			replace(user1in1)
			count = count + 1
# user1in1 = input("User 1 select your move: ")
#user1in1 is user input 1
replace("X")

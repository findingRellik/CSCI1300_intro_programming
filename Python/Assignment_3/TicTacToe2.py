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
'''
print ("   |   |   ")
print ("_1_|_2_|_3_")
print ("_4_|_5_|_6_")
print ("_7_|_8_|_9_")
print ("   |   |   ")
'''
line0 = ("   |   |   ")
line1 = ("_1_|_2_|_3_")
line2 = ("_4_|_5_|_6_")
line3 = ("_7_|_8_|_9_")
line4 = ("   |   |   ")
'''
line0 = ("     |    |   ", )
line1 = ("_",sqr1,"_|",sqr2,"_|_",sqr3,"_")
line2 = ("_",sqr4,"_|",sqr5,"_|_",sqr6,"_")
line3 = ("_",sqr7,"_|",sqr8,"_|_",sqr9,"_")
line4 = ("      |    |   ")
print (line0)
print (line1)
print (line2)
print (line3)
print (line4)
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
def showBoard():
	print ("     |    |   ")
	print ("_",sqr1,"_|",sqr2,"_|_",sqr3,"_")
	print ("_",sqr4,"_|",sqr5,"_|_",sqr6,"_")
	print ("_",sqr7,"_|",sqr8,"_|_",sqr9,"_")
	print (      |    |   ")
	line0 = ("             |           |   ")
	line1 = ("_",sqr1,"_|_",sqr2,"_|_",sqr3,"_")
	line2 = ("_",sqr4,"_|_",sqr5,"_|_",sqr6,"_")
	line3 = ("_",sqr7,"_|_",sqr8,"_|_",sqr9,"_")
	line4 = ("             |           |   ")
'''

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
'''	
	print (line0)
	print (line15)
	print (line25)
	print (line35)
	print (line4)
'''	
	
	
#showBoard()

#user1in1 = str(input("User 1 select your move: "))
#user1in1 is user input 1
#user2in1 = input(" select your move: ")
#userin = 0

'''	
	if user1in1  == "1":
		line15 = line1.replace(sqr1,"X")
	elif user1in1 == "2":
		line15 = line1.replace(sqr2,"X")
	elif user1in1 == "3":
		line15 = line1.replace(sqr3,"X")
	elif user1in1 == "4":
		line25 = line2.replace(sqr4,"X")
	elif user1in1 == "5":
		line25 = line2.replace(sqr5,"X")
	elif user1in1 == "6":
		line25 = line2.replace(sqr6,"X")
	elif user1in1 == "7":
		line35 = line3.replace(sqr7,"X")
	elif user1in1 == "8":
		line35 = line3.replace(sqr8,"X")	
	elif user1in1 == "9":
		line35 = line3.replace("9","X")
	else: print("Error")	
	showBoard()
	if var  == "1":
		var = var.replace("1","X")
	elif var == "2":
		line15 = line1.replace("2","X")
	elif var == "3":
		line15 = line1.replace("3","X")
	elif var == "4":
		line25 = line2.replace(sqr4,"X")
	elif var == "5":
		line25 = line2.replace(sqr5,"X")
	elif var == "6":
		line25 = line2.replace(sqr6,"X")
	elif var == "7":
		line35 = line3.replace(sqr7,"X")
	elif var == "8":
		line35 = line3.replace(sqr8,"X")	
	elif var == "9":
		line35 = line3.replace("9","X")
	else: 
		print("Error")	
'''
line0 = ("             |           |   ")
line15 = ("_",sqr1,"_|_",sqr2,"_|_",sqr3,"_")
line25 = ("_",sqr4,"_|_",sqr5,"_|_",sqr6,"_")
line35 = ("_",sqr7,"_|_",sqr8,"_|_",sqr9,"_")
line4 = ("             |           |   ")

def replaceNumber(var):
	line0 = ("             |           |   ")
	line1 = ("_",sqr1,"_|_",sqr2,"_|_",sqr3,"_")
	line2 = ("_",sqr4,"_|_",sqr5,"_|_",sqr6,"_")
	line3 = ("_",sqr7,"_|_",sqr8,"_|_",sqr9,"_")
	line4 = ("             |           |   ")
	if var  == "1":
		line15 = line1.replace("1","X")
	elif var == "2":
		line15 = line1.replace("2","X")
	elif var == "3":
		line15 = line1.replace("3","X")
	elif var == "4":
		line25 = line2.replace("4","X")
	elif var == "5":
		line25 = line2.replace("5","X")
	elif var == "6":
		line25 = line2.replace("6","X")
	elif var == "7":
		line35 = line3.replace("7","X")
	elif var == "8":
		line35 = line3.replace("8","X")	
	elif var == "9":
		line35 = line3.replace("9","X")
	else: 
		print("Error")	
	print (line0)
	print (line15)
	print (line25)
	print (line35)
	print (line4)
	
showBoard()

user1in1 = str(input("User 1 select your move: "))
	
replaceNumber(user1in1)


'''
#def askUserinput():
	#user1in =
'''	
'''
user1in1 = input(user1, " select your move: ")
#user1in1 is user input 1
user2in1 = input(user2, " select your move: ")

user1in2 = input(user1, " select your move: ")
user2in2 = input(user2, " select your move: ")

user1in3 = input(user1, " select your move: ")
user2in3 = input(user2, " select your move: ")

user1in4 = input(user1, " select your move: ")
user2in4 = input(user2, " select your move: ")

user1in5 = input(user1, " select your move: ")
'''
'''
import os, sys

exts = ['.py', '.ini', '.c', '.h']
count_empty_line = True
here = os.path.abspath(os.path.dirname(sys.argv[0]))

def read_line_count(fname):
    count = 0
    for line in open(fname).readlines():
        if count_empty_line or len(line.strip()) > 0:
            count += 1
    return count
if __name__ == '__main__':
    line_count = 0
    file_count = 0
    for base, dirs, files in os.walk(here):
        for file in files:
            # Check the sub directorys            
            if file.find('.') < 0:
                continue
            ext = (file[file.rindex('.'):]).lower()
            try:
                if exts.index(ext) >= 0:
                    file_count += 1
                    path = (base + '/'+ file)
                    c = read_line_count(path)
#                    print ".%s : %d" % (/[len(here):], c)
                    line_count += c
            except:
                pass
#    print 'File count : %d' % file_count
    print 'Line count : %d' % line_count
'''

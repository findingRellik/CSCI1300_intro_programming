#Assignment 2 Football problem //Python3
#Recitation 10 am ECCR 235
#Austin Metzner

name = raw_input("Enter the quarterback's name you'd like to find the rating of: ")
c = int(input("Enter completions: "))
a = int(input("Enter attempts: "))
y = int(input("Enter yards: "))
td = int(input("Enter number of touchdowns: "))
i = int(input("Enter number of interceptions: "))

C = ((c/a)-.3)*5
Y = ((y/a)-3)*.25
T = ((td/a)*20)
I = 2.375-((i/a)*25)


#part X: I didn't attempt to use "or" in attempt
#to shorten this part of the code
if C < 0:
	print C, "is C"
	C = 0
	print ("Negative changed to 0")
if Y < 0:
	print Y, "is Y"
	Y = 0
	print ("Negative changed to 0")
if I < 0:
	print I, "is I"
	I = 0
	print ("Negative changed to 0")
if T < 0:
	print T, "is Y"
	T = 0
	print ("Negative changed to 0")

#Part XI: copied the last part of code
if C > 2.375:
	C = 2.375
	print (C, "Changed to 2.375")
if Y > 2.375:
	Y = 2.375
	print (Y, "Changed to 2.375")
if I > 2.375:
	I = 2.375
	print (I, "Changed to 2.375")
if T > 2.375:
	T = 2.375
	print (T, "Changed to 2.375")

#Part XII: Calculating the score
pr = (C+Y+T+I)/6*100
print ("Looks like ", name, "has a QB rating of: %.2f" % pr)

#After the rating is printed calculate whether they are good or not
if pr < 85:
	print ("This QB's rating is poor!")
if 85 < pr < 90:
	print ("This QB's rating is good!")
if 90 < pr:
	print ("This QB's rating is great!")

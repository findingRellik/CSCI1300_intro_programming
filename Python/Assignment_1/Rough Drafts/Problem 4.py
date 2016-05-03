#A	day	has	86,400	seconds	(24*60*60).	Given	a	number	in	the	range	of	
#86,400,	output	the	current	time	as	hours,	minutes,	and	seconds	for	a	24-hour	
#clock.	For	example,	70,000	seconds	is	19	hours,	26	minutes,	and	40	seconds.	
#Your	program	should	have	one	user	input that	is	the	number	of	seconds	to	
#convert,	and	then	use	that	number	in	your	calculations.	Your	output	should	

t = int(input("Pick a number between 0 and 86,400:"))

#To get the hours, divide by 3600
h = (t/(60*60))
print(h)

#To get minutes, divide remainder of hours calculation by 60
m = (t%(60*60))/60

#This gets the remainder of the minutes calculation is the seconds
#r1 is the remaining seconds after finding the hours
r1 = (t%(60*60))
#print (r1)
print (m)

#(r1%60) is the is the remaining seconds
s = (r1%60)
print (s)

print ("The time is ", h, "hours, ", m, " minutes, and ", s, "seconds!")

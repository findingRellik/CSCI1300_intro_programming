
#fresh	surface	water. Write	a	program	to	calculate	how	deep	it	would	be	if	all	

#contiguous	U.S.	states.	You	will	need	to	do	some	Internet	research	to	
#determine	the	area	of	that	region.	Your	output	should	be	displayed	in	meters,	

#meters.	You	will	need	to	look	up	format	specifiers	in	Python	to	print	a	value	
#with	two	decimal	places.

# Area of 48 states 3,119,884.69 sq miles
#22,810	km3 
# 8,080,464.3 km sq

w = 22810
#w is water
a = 8080464.3
#a is area
print "There is ", w, " km^3 of water in the Great Lakes."
print "That means if this water was spread across all 48 contiguous"
a = (w/a)*1000
#("%.2f" % (variable) a) is the format specifier I used
print "states, it would be ", ("%.2f" % a), " meters deep everywhere."



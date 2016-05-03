#The	U.S.	Census	provides	information	about	the	current	U.S.	population	as	
#well	as	approximate	rates	of	change.	Three	rates	of	change	are	provided:
#a. There	is	a	birth	every	7	seconds
#b. There	is	a	death	every	13	seconds
#c. There	is	a	new	immigrant	every	35	seconds
#Using	those	three	rates	of	change,	and	a	current	U.S.	population	of	
#307,357,870,	write	a	program	to	calculate	the	U.S.	population	in	exactly	one	
#year (365	days). Your	program	should	output	the	result	in	a	nicely	formatted	

#310,338,194.
#Hints:	You	will	need	to	calculate	the	number	of	seconds	in	one	year. Also,	a	
#population	cannot	have	fractional	people,	e.g	there	can	be	10	people,	but	not	
#10.2	people.

#sp = starting population

sp = 307357870

t = int(input("Population after how long (years)?: "))

n = t*365*24*60*60

a = round(n/7)
b = round(n/35)
c = round(n/13)

print ("The	population will	be:v")
Pop = (sp+a+b-c)
print (Pop)
print "In ", t,"years"

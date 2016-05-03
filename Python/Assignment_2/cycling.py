#Assignment 2 Football problem
#Recitation 10 am ECCR 235
#Austin Metzner

print ("Cycling: power and energy")
m = float(input("Enter mass of cyclist (kg): "))
mb = float(input("Enter mass of bike (kg): "))
v = float(input("Enter velocity (m/s): "))
g = 9.8
k = .18
cr = .001
cf = float(input("Enter CFdraft: "))
#assuming the avg. between .6 and .8

#         Not sure what to do for CFdraft
#cfq = input("Is cyclist at front of pack?(y/n): ")
#if cfq == "y" or "Y":
#	cf = 1.0
#	elif cfq == "n" or "N":
#		print (" ")
#	else: 
#		print ("Not a valid input")
	
#Pair	
pa = k*cf*v**3
#Proll
pr = cr*g*(m+mb)*v
#Psec
ps = pr+pa

####print ("Total power output per second: ", "%.2f" % ps)

d = float(input("Distance needed to travel (km): "))
#timeTravel in seconds
tt = ((d*1000)/v)
#Energytotal = Psec * timeTravel = et
et = round(ps*tt)
####print ("Total energy output is: ", et)

#Energy per minute

tt = int((d*1000)/(v*60))
#to get timeTraveled in minutes
et = 0
x = 0
import random

while x < tt:

	cf = random.uniform(0.5,1)
	pa = k*cf*v**3
	
#recalling pa to be inside while loop
	pm = round(ps*60)
#	energy = (pm*x)
#pm is ps per min
	print ("Energy at ", x, " minute: ", energy)
#	energy = round(pm * tt)
	
	et += energy
	print ("Total energy at ", x, " minute: ", et, "Joules")
	x += 1
#	if x == tt:
#		pause ()
	



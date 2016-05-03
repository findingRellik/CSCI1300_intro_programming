#!/usr/bin/env	python
#Assignment 6 
from geopy.geocoders import OpenMapQuest
from geopy import Point
from geopy.distance import vincenty

import sys

geolocator = OpenMapQuest()
totalDist = 0

def main():
	cl = open(sys.argv[1], "r") #cl = citylist
	cl = cl.readlines()
	lPlaces = [] #list of places
	lPlacesCorrect = []
	lPlacesVisited = []
	totalDist = 0
	counter = 0
	minDistCity = ""
	minDist = 7999999
	for line in cl:
		lPlaces.append(line.rstrip("\n"))
	currentCity = lPlaces[0]
	lPlacesCorrect.append(currentCity)
	while len(lPlaces) != len(lPlacesCorrect):
		counter = 0
		minDist = 7999999
		while counter < len(lPlaces):
			if lPlaces[counter] not in lPlacesCorrect:
				distanceBetweenCities = getDistance (lPlaces[counter],currentCity)
				#print lPlaces[counter]
				#print distanceBetweenCities
				if distanceBetweenCities < minDist and distanceBetweenCities != 0:
					minDist = distanceBetweenCities
					minDistCity = lPlaces[counter]
			counter += 1
					
		#lPlaces.remove(minDistCity)
		totalDist += minDist
		currentCity = minDistCity
		lPlacesCorrect.append(currentCity)
		#print totalDist
		#print lPlacesCorrect[0:]
		#print lPlaces[0:]
	#lPlacesCorrect.append(lPlaces[0])
	lastDist = getDistance(lPlaces[0],lPlacesCorrect[-1])
	#print lPlaces[0]
	#print lPlacesCorrect[-1]
	#print lastDist
	finalDist = totalDist + lastDist 
	print lPlacesCorrect
	print finalDist
	
def getDistance(Input1,Input2):
	
	address1, (lat1, lon1) = geolocator.geocode(Input1)
	address2, (lat2, lon2) = geolocator.geocode(Input2)
	distanceBetweenCities = vincenty ((lat1, lon1), (lat2, lon2)).miles
	distance = distanceBetweenCities
	return distance
	
main()

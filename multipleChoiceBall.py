#!/usr/bin/env python

from random import *

def multipleChoiceBall():
    numberOfChoices = raw_input("How many options do you have to choose from? [integer] ")
    listOfChoices = []
    for n in range(int(numberOfChoices)):
	choice = raw_input("Enter choice " + str(n+1) + ": ")
	listOfChoices.append(choice)
    choiceIndex = randint(0, len(listOfChoices)-1)
    print "You should select " + listOfChoices[choiceIndex] + "! "

multipleChoiceBall()

# usage: python magic8ball.py
from random import *

def magic8ball():
    answer = raw_input("Is your question related to science? (Yes or No) ")
    science_responses = ["Grep it", "C1V1 = C2V2", "ssh 10.1.1.1", "> 60,000 Kb"]
    general_responses = ["What would Justin Trudeau do?", "Eat a taco.", "Look in your heart."]
    if answer.lower() != "yes" and answer.lower() != "no":
        print "You're a dummy who cannot follow instructions and don't deserve answers. "
    if answer.lower() == "yes":
        question = raw_input("What is your question? ")
        response_index = randint(0, len(science_responses)-1)
        print science_responses[response_index]
    if answer.lower() == "no":
        question = raw_input("What is your question? ")
        response_index = randint(0, len(general_responses)-1)
        print general_responses[response_index]

magic8ball()

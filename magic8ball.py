# usage: python magic8ball.py
from random import *

def magic8ball():
    question = raw_input("What is your question? ")
    responses = ["Grep it", "C1V1 = C2V2", "ssh 10.1.1.1", "What would Justin Trudeau do?", "Eat a taco.", "Look in your heart."]
    how_responses = ["Grep it", "ssh 10.1.1.1", "What would Justin Trudeau do?", "Look in your heart.", "One leg at a time."]
    who_responses = ["Justin Trudeau", "Your momma", "Who do you think?", "A loser", "A winner"]
    whatis_responses = ["Tacos"]
    if question.lower().startswith('how'):
        response_index = randint(0, len(how_responses)-1)
        print how_responses[response_index]
    elif question.lower().startswith('who'):
        response_index = randint(0, len(who_responses)-1)
        print who_responses[response_index]
    elif question.lower().startswith('what is'):
        response_index = randint(0, len(whatis_responses)-1)
        print whatis_responses[response_index]
    else:
        response_index = randint(0, len(responses)-1)
        print responses[response_index]
magic8ball()

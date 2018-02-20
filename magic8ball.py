#!/usr/bin/env python

from random import *

def magic8ball():
    question = raw_input("What is your question? ")
    yesno_responses = ["Justin Trudeau is certain.", "As Justin Trudeau sees it, yes.", "Reply hazy try again.", "Don't count on it.", "Justin Trudeau decided it so.", "Justin Trudeau thinks so.", "Justin Trudeau wants you to ask again later.", "Justin Trudeau's reply is no.", "Justin Trudeau has no doubt.", "Outlook good.", "Better not tell you now.", "Justin Trudeau says no.", "Yes, definitely.", "Yes.", "Cannot predict now.", "Outlook not so good.", "You may rely on it", "Justin Trudeau points to yes.", "Concentrate and ask Justin Trudeau again.", "Justin Trudeau doesn't think so."]
    responses = ["Grep it", "C1V1 = C2V2", "ssh 10.1.1.1", "What would Justin Trudeau do?", "Eat a taco.", "Look in your heart."]
    how_responses = ["Grep it", "ssh 10.1.1.1", "What would Justin Trudeau do?", "Look in your heart.", "One leg at a time."]
    who_responses = ["Justin Trudeau", "Your momma", "Who do you think?", "A loser", "A winner"]
    whatis_responses = ["Tacos", "42"]
    if question.lower().startswith('is') or question.lower().startswith('should') or question.lower().startswith('could') or question.lower().startswith('will'):
        response_index = randint(0, len(yesno_responses)-1)
        print yesno_responses[response_index]
    elif question.lower().startswith('how'):
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

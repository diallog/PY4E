#!/usr/bin/env python3

# PURPOSE: counts occurences of a character in a string

import os
os.system('clear')

# define function
def stringSearch():
    occurence = 0
    s = input("Provide a string, e.g phrase, song lyric: ")
    c = input("Provide a single character to search for in the string: ")
    userString = s.lower()
    userCharacter = c.lower()

# don't waste time, check to see if Character is in String before proceeding
    if userCharacter not in userString:
        print("The character '{character}' does not occur in the the string '{string}'."
              .format(character = userCharacter, string = userString))
    else:
        for character in userString:
            # does the string character match userCharacter?
            if character == userCharacter:
                occurence += 1
        print("The character '{character}' occurs {occurence} times in the string '{string}'."
              .format(character = userCharacter, occurence = occurence, string = userString.capitalize()))

# execute function
stringSearch()

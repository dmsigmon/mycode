#!/usr/bin/env python3

def twostrings():
    """Create a function that will accept two strings.
     Have the function return a single string after having the two strings inputted combined around
     the phrase "the last time I was in a porta-potty"""

    s1 = input('give a random sentence:  ')
    s2 = input('give another random sentence:  ')

    print(f'{s1} the last time I was in a porta-potty {s2}')

twostrings()

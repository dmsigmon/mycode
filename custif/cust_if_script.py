#!/usr/bin/env python3

message = 'Your connection speed is '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 500:
    message = message + 'amazingly fast, you must be a gamer or IT Pro'
elif connection >= 300:
    message = message + 'could be better but your still moving pretty fast'
elif connection >= 100:
    message = message + 'standard and will probably suffice for most people'
elif connection >= 50:
    message = message + 'a bit slow, you deseve better'
elif connection >= 10:
    message = message + 'kinda slow, my gradnma has faster speeds than this. lets get you upgraded'
else:
    message = message + 'legacy. Seek help immediately'
print(message)

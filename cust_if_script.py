#!/usr/bin/env python3

"""Movie rating perfection standards by person"""


message = 'The movie you just watched '

# wrap connection in a float() to accept decimals as numbers
rating = float(input("What is your movie rating? On a scale of 1-10, 1 worst, 10 best: "))

# if input value was higher or equal to 10
if rating >= 10:
    message = message + 'is up to Kent perfection standards.'
elif rating >= 5:
    message = message + 'is up to Dan perfection standards.'
elif rating >= 2:
    message = message + 'is up to Wes perfection standards.'
else:
    message = message + 'is up to Jeff perfection standards.'
print(message)

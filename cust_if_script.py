#!/usr/bin/env python3

"""Movie rating perfection standards by person"""


message = 'The movie you just watched '

# wrap connection in a float() to accept decimals as numbers
rating = float(input("What is your movie rating? On a scale of 1-10, 1 worst, 10 best: "))

# if input value was higher or equal to 10
if rating == 42:
    print('Where you are going, you wont need a guide. Now go hitch a ride!')
elif rating >= 10:
    message = message + 'is up to Kent perfection standards.'
    print(message)
elif rating >= 5:
    message = message + 'is up to Dan perfection standards.'
    print(message)
elif rating >= 2:
    message = message + 'is up to Wes perfection standards.'
    print(message)
else:
    message = message + 'is up to Jeff perfection standards.'
    print(message)

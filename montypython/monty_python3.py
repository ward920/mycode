#!/usr/bin/env python3
  
# Counter control for loop
round = 0
answer = " "

# Simple loop
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    answer = answer.capitalize()
    if answer == 'Kent':
        print('Correct!')
        break
    elif answer == "Shrubbery":
        print('You gave the super secret answer!')
    elif round == 3:
        print('Sorry the answer was Kent')
        break
    else:
        print('Sorry try again')

import random
number=random.randint(1,9)
print("number guessing game")
print("guess a number(between 1 and 9)")
chances=0
while chances < 5:
    guess=int(input("enter your number"))

    if guess==number:
        print("congradulations! You Won!") 
        break

    elif guess > number:
        print("your guess is too hight,pick a lower number")

    else: print("your number was too low, guess a higher number")
    chances=chances+1

    if not chances < 5:
        print("you lose, the number is",number)
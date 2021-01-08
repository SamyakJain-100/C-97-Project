import random

print("WELCOME TO GUESSING GAME")

rand = random.randint(1,9)

chances = 0

print("GUESS A NUMBER BETWEEN 1 To 9")

while chances<5:
    
    guess = int(input("ENTER THE NUMBER TO GUESS"))

    
    if guess == rand:
        print("CONGRATS! YOU GUESSED IT RIGHT")
        break
    
    
    elif guess < rand:
        print("YOUR GUES IS TOO LOW")
        print("GUESS A NUMBER HIGHER THAN THIS")

    else:
        print("YOUR GUESS IS TOO HIGH.")
        print("GUESS A NUMBER LESS THAN THIS")
    
    
    chances+=1

if chances==5 and guess!= rand:
    print("YOU LOSE")
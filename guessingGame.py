import random

chances = 0
number = random.randint(1,10)

while chances < 5:
    guess = int(input("guess the number! hint: it is somewhere between 1 and 10: "))

    if(guess == number):
        print("You Won! Congratulations!!")        
        break
    
    elif(guess < number):
        print("your guess was too low, guess higher!!")

    else:
        print("your guess was too high, guess lower!!") 
        
    chances = chances + 1

    if not chances < 5:
        print("You Lose! Too bad, the number was ", number)


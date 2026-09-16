import random 
print()
print("---Guess the number---")
playing=True
num=random.randint(1,10)
print()
print("Guess a number between 1 and 10.")
while playing:
    guess=int(input("Enter your guess: "))
    if guess==num:
        print("You guessed correctly!\nWell done!")
        break
    else:
        print("You got it wrong!\nTry again!")

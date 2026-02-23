import random
secret_number=random.randint(0,10)
attempts=0
print('Guessing a number between 1 and 10')
while True: 
    guess=int(input("Enter your guess"))
    attempts+=1
    if guess==secret_number:
        print("You quessed right.")
        print("Attempts:",attempts)
        break
    elif guess<secret_number:
        print("Too low,Try again.")
    else:
        print("Too high, Try again")


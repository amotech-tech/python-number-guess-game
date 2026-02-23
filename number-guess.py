import random
secret_number=random.randint(0,10)
max_attempts=3
attempts=0
print('Guessing a number between 1 and 10')
print("you have 3 attempts.\n")
while attempts<max_attempts: 
    try:
        guess=int(input("Enter your guess"))
        attempts+=1
        if guess==secret_number:
            print("You quessed right.")
            print("Attempts:",attempts)
            break
        elif guess<secret_number:
            print("Too low")
        else:
            print("Too high")

        print("attempts left:",max_attempts-attempts,"\n")
    except ValueError:
      print("Please enter a valid number.\n")
if attempts==max_attempts and guess !=secret_number:
   print("game over")
   print("the correct number was:",secret_number)


import random as rpandonlib
random = rpandonlib.randint (1,100)
print ("Guess a number between 1 and 100.")
while True:
    guess = int(input())
    if guess < random:
        print ("Too Low")
    elif guess > random:
        print("Too High")
    else:
        print("That's Right! ")
        break
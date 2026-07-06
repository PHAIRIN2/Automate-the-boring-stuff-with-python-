import random

SecretNumber = random.randint(1, 20)
print("I am tinking of a number between 1 and 20.")

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < SecretNumber:
        print("You guess is too low.")
    elif guess > SecretNumber:
        print("You guess is too high.")
    else:
        break
if guess == SecretNumber:
    print("Good JOB! you guessed my number in " + str(guessesTaken) + "")
else:
    print("Nope. the number I was thinking of was " + str(SecretNumber) + "")

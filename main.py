import random

name = input("Enter your name: ").capitalize()
print(f"Hi {name}. Welcome to guess a number game !!")
alert = input("Do you want to play this game (yes/no) ?? ").lower()

score = 0
guesses = 0

if alert == "yes":
    times_play = int(input("How many times do you want to play: "))

    for i in range(times_play):
        number = random.randint(1, 100)
        user_number = int(input("Enter a number between 1 and 100: "))
        if number == user_number:
            print("Correct !!")
            print(f"The correct answer is: {number}")
            score += 1
            guesses += 1
        else:
            print("Wrong !!")
            print(f"The correct answer was: {number}")
            guesses += 1
        
    print()
    print(f"Your total score: {score}")
    print(f"Your total number of guesses: {guesses}")

elif alert == "no":
    print("Thank you for using !!!")
    print("Bye !!")

else:
    print("Only use (yes) or (no)")
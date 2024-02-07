import random
ran = random.randint(1, 20)
name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
num = int(input())
guesses = 1
while num != ran:
    if num > ran:
        print("Your guess is too big.")
        print("Take a guess.")
        guesses += 1
    elif num < ran:
        print("Your guess is too low.")
        print("Take a guess.")
        guesses += 1
    num = int(input())

print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
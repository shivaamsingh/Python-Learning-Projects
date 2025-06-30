import random

top_range = int(input("Type a number: "))

if top_range <= 0:
    print("Please type a number greater than 0 next time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Make a guess: "))

    if user_guess == random_number:
        print("🎉 You got it!")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print(f"✅ You got it in {guesses} guesses!")

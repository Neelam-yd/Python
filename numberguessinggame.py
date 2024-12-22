import random

number_to_guess = random.randrange(100)  # Random number between 0 and 99
chances = 7  # Total chances available
guess_counter = 0  # Start with 0 guesses

print("Guess the number (between 0 and 99):")

while guess_counter < chances:  # Loop until all chances are used
    try:
        guess = int(input(f"Chance {guess_counter + 1} of {chances}: Enter your guess: "))
        guess_counter += 1  # Increment the counter for each guess
        
        if guess == number_to_guess:
            print(f"🎉 Congratulations! Your guess is correct. The number was {number_to_guess}.")
            break  # Exit the loop if the guess is correct
        elif guess > number_to_guess:
            print("Your guess is too high. Try again!")
        else:
            print("Your guess is too low. Try again!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if guess_counter == chances and guess != number_to_guess:
    print(f"😢 Sorry, you've used all your chances. The correct number was {number_to_guess}.")

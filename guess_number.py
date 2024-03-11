number = 10
max_guesses = 3
guess_count = 0

while True:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? (Enter 'q' to quit): ")

    if guess.lower() == 'q':
       print(f"The number was {number}")
       break

    try:
       guess_input = int(guess)
    except ValueError:
       print("Enter a valid number or 'q' to quit.")
       continue

    guess_count += 1

    if guess_input == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess_count < max_guesses:
        print(f"That's incorrect. You have {max_guesses - guess_count} {'guesses' if max_guesses - guess_count > 1 else 'guess'} left. Try again.")
    else:
        print(f"Sorry! You ran out of guesses. The number was {number}.")

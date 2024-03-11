number = 10

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

    if guess_input == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess_input < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

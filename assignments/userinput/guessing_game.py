def start():

    answer = "Giraffe".lower()
    guess = None
    tries = 3
    attempt = 0
    print("This is a Guessing Game! You have 3 tries to guess the animal that I am thinking of. What is a tall animal with black spots and a long neck?")

    while attempt < tries:
        guess = input("Enter your best guess: ").lower()
        attempt += 1
        if guess == answer:
            print(f"You guessed correctly! The answer is {answer}!")
            break
        elif guess == "quit":
            print("Goodbye!")
        elif attempt == 3:
            print(f"Im sorry, you lost.")
            break
        else:
            print("You can try again! You have", 3 - attempt, "guesses left!")

    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    return (None)  # replace this line with your game loop logic.


start()

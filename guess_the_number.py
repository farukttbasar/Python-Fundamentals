import time
import random


while True:
    try:
        game_request = int(input("Do you want to play a 'Guess the Number' game? (1 - YES , 2 - NO) "))
    except ValueError:
        print("\nInvalid input! Please enter only 1 or 2.")
        continue

    if game_request == 2:
        print("See you...")
        break
    elif game_request == 1:
        print("- - WELCOME TO 'GUESS THE NUMBER' GAME - -")
        lives = 5
        the_number = random.randint(1,40)

        print("Thinking of a number...")
        for i in range(3,0,-1):
            print(f"{i}...")
            time.sleep(0.5)

        while lives > 0:
            print(f"\nLives left: {'❤️' * lives}")
            
            try:
                the_guess = int(input("Invalid input! Please guess a number between 1 and 40 (inclusive): "))
            except ValueError:
                print("Invalid input! Please enter number only!")
                continue

            if 1 > the_guess or the_guess > 40:
                print("Out of range! Please enter a number between 1 and 40 (inclusive): ")
                continue
           
            if the_guess == the_number:
                print("\n" + "*" * 40)
                print("CONGRATULATIONS! YOU WON THE GAME! 🏆")
                print("*" * 40)
                break
            elif the_guess < the_number:
                print("The number is HIGHER than your guess. ")
            else:
                print("The number is LOWER than your guess. ")

            lives -= 1

        if lives == 0:
            print("\n" + "*" * 20)
            print("     GAME OVER")
            print("*" * 20)
            print(f"The hidden number was: {the_number}")
            print("Better luck next time!")

    else:
        print("Invalid input! Please enter 1 or 2 (consider the choices). ")

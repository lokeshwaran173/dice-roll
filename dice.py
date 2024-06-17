import random  # Import the random module

MIN_VAL, MAX_VAL = 1, 6  # Range of the values of a dice
roll_again = "yes"  # To loop the rolling through user input

while roll_again.lower() in ("yes", "y"):  # Loop
    print("Rolling The Dices...")
    print("The Values are:")
    
    # Generating and printing two random integers from 1 to 6
    print(random.randint(MIN_VAL, MAX_VAL))
    print(random.randint(MIN_VAL, MAX_VAL))
    
    # Asking user to roll the dice again. Any input other than 'yes' or 'y' will terminate the loop
    roll_again = input("Roll the Dices Again? (yes/y to continue): ").strip().lower()

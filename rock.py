import random

# Print multiline instruction
print('Mechanics and rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock ✊  vs Paper ✋-> Paper ✋ wins\n"
      + "Rock ✊ vs Scissors ✌️ -> Rock ✊  wins \n"
      + "Paper ✋ vs Scissors ✌️ -> Scissors ✌️ wins \n"  + "Same Choice = Tie or Draw 🤝\n")

def play_game():
    while True:

        print("Enter your choice \n Rock '✊' = 1 \n Paper '✋'= 2\n Scissors '✌️' = 3\n")

        # Take the input from user
        choice = int(input("Enter your choice: "))

        # Looping until user enters valid input
        while choice > 3 or choice < 1:
            choice = int(input('Error, Please Enter a valid Choice: '))

        # Initialize value of choice_name variable corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
            choice_icon = '✊'
        elif choice == 2:
            choice_name = 'Paper'
            choice_icon = '✋'
        else:
            choice_name = 'Scissors'
            choice_icon = '✌️'

        # Print user choice
        print('User choice is:', choice_name, choice_icon ," \n")
        print("Now it's Opponent's Turn..." ," \n")

        # Computer chooses randomly any number among 1, 2, and 3
        comp_choice = random.randint(1, 3)

        # Initialize value of comp_choice_name variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
            comp_choice_icon = '✊'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
            comp_choice_icon = '✋'
        else:
            comp_choice_name = 'Scissors'
            comp_choice_icon = '✌️'

        print("Opponent's choice is:", comp_choice_name, comp_choice_icon," \n")
        print(choice_name, 'vs', comp_choice_name)

        # Determine the winner
        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Paper'
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = 'Rock'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Scissors'

        # Print the result
        if result == "DRAW":
            print("<== It's a tie! 🤝 ==>")
        elif result == choice_name:
            print("<== User wins! 🏆 ==>")
        else:
            print("<== Your Opponent's wins! 🏆 ==>")

        # Ask if the user wants to play again
        while True:
            play_again = input("Do you want to play again? (Y/N): ").strip().lower()
            if play_again in["yes", "y"]:
                break
            elif play_again in["no", "n"]:
                print("Thanks for playing! Goodbye.")
                return
            else:
                print("Invalid Input, Enter Yes or No Only: ")
                
if __name__== "__main__":
    play_game()

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")
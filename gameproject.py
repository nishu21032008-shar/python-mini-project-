import random

# Project 2: Simple Game (Stone-Paper-Scissors & Dice Roll)

# Function for Stone-Paper-Scissors Logic
def stone_paper_scissors():
    print("\n--- Stone-Paper-Scissors ---")
    options = ["Stone", "Paper", "Scissors"]
    user_choice = input("Enter your choice (Stone, Paper, Scissors): ").capitalize()
    
    if user_choice not in options:
        print("Invalid choice! Please try again.")
        return

    comp_choice = random.choice(options)
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a Draw! 🤝")
    elif (user_choice == "Stone" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Stone") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        print("Congratulations! You Win! 🎉")
    else:
        print("Computer Wins! Better luck next time. 🤖")

# Function for Dice Roll Logic
def dice_roll():
    print("\n--- Dice Roll Game ---")
    input("Press Enter to roll the dice...")
    number = random.randint(1, 6)
    print(f"You rolled a: {number}")
    if number == 6:
        print("Excellent! You got a 6! ⭐")
    else:
        print("Nice roll!")

# Main Menu System (Infinite Loop)
def main_menu():
    while True:
        print("\n==========================")
        print("      GAME ZONE MENU      ")
        print("==========================")
        print("1. Play Stone-Paper-Scissors")
        print("2. Play Dice Roll")
        print("3. Exit")
        
        choice = input("\nSelect an option (1/2/3): ")

        if choice == '1':
            stone_paper_scissors()
        elif choice == '2':
            dice_roll()
        elif choice == '3':
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid option! Please select 1, 2, or 3.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
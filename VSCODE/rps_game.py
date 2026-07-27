import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    score_user = 0
    score_comp = 0

    print("==== Rock Paper Scissors Game ====")
    print("Rules: rock > scissors, scissors > paper, paper > rock")
    print("Exit karne ke liye 'quit' likho\n")

    while True:
        user_choice = input("Tumhari choice: rock / paper / scissors: ").lower()
        
        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("Galat input! rock, paper ya scissors likho\n")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer ne chuna: {comp_choice}")

        # game logic
        if user_choice == comp_choice:
            print("Draw! 🤝")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "scissors" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "rock"):
            print("Tum jeet gaye! 🎉")
            score_user += 1
        else:
            print("Computer jeet gaya! 😅")
            score_comp += 1

        print(f"Score - Tum: {score_user} | Computer: {score_comp}\n")

    print("\nFinal Score:")
    print(f"Tum: {score_user} | Computer: {score_comp}")
    print("Game khatam. Thanks for playing!")

play_game()
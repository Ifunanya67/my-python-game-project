import random

while True:
    print("welcome to Rock, Paper, scissors Game")

    user_action = input("Enter a choice (rock, paper,scissors): ")
    possible_actions = ("rock", "paper", "scissors")
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer_chose {computer_action}.\n")

            #determining the winner
    if user_action == computer_action:
     print(f"Both players selected {user_action}. It's a tie")

    elif user_action == "rock":
      if computer_action == "scissors":
        print("rock smashes scissors, You Win.")
      else:
        print("paper covers rock, You Lose")


    elif user_action == "paper":
      if computer_action == "rock":
        print("paper covers rock, You Win")
      else:
        print("scissors cuts paper, You Lose")

    elif user_action == "scissors":
      if computer_action == "paper":
        print("scissors cuts paper You Win")
      else:
        print("Rock smashes scissors, You Lose")


    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
   
    


   


    

    
    
    
import random

def pao_ying_chub():

    print("let's play game!")
    hand = ["hammer", "paper", "scissors"]
    com_hand = random.choice(hand)
    player_hand = input("Please choose your hand (hammer, paper, or scissors): ")

    ## Check Input
    while player_hand not in hand:
        print("------")
        print("Invalid input. Please choose again.")
        print("------")
        player_hand = input("Please choose your hand (hammer, paper, or scissors): ")

    print("------")
    print(f"Player: {player_hand}")
    print(f"CPU: {com_hand}")

    ## Find the Winner
    if com_hand == player_hand:
        result = "It's a tie!"
    elif (com_hand == "hammer" and player_hand == "scissors") or \
         (com_hand == "scissors" and player_hand == "paper") or \
         (com_hand == "paper" and player_hand == "hammer"):
        result = "You lose!"
    else:
        result = "You win!"

    # Print the result
    print("------")
    print(result)

pao_ying_chub()

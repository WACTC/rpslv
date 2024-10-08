#
#           project:    rps.py
#            author:    Charles J McDonald <cmcdonald@woonsocketschools.com>
#           version:    2.0
#   last updated on:    10/8/2024
#
#   description: Rock, Paper, Scissors, Lizard, Spock for 2 players
#

# === Introduce the Game
# Rules = Rock, Paper, or Scissors
print("""
=== RPS Duel === \n
    Challengers, step forward and prepare thyselves for an epic duel!!!
""")

# === Get the names of our challengers
player1 = input("First Challenger, what is thy name? : ")
player2 = input("Second Challenger, what is thy name? : ")
score1 = score2 = 0
isPlaying = True

while isPlaying:
    # === Choose your move
    print("""
    On yon table before thee reste weapons three:
        [R]ock : An ancient weapon of destruction
        [P]aper: An elegant weapon for the literate
        [S]cissors: A brutish blade for the stylish
        [L]izard: A deadly reptile from the far realms
        [V]Spock: A being of ineffable logic
    """)

    weapon1 = input(f"{player1}, choose thy weapon! : ")
    weapon2 = input(f"{player2}, choose thy weapon! : ")

    # === Resolve combat
    if weapon1 == "R" :     #   Player1 chooses Rock
        if weapon2 == "R" :
            print("Thou hast ended in a Draw!")
        elif weapon2 == "P":
            print(f"Paper covers Rock! {player2} wins this round!")
            score2 = score2 + 1
        elif weapon2 == "V":
            print(f"Spock vapourizes Rock with his phaser! {player2} wins this round!")
            score2 = score2 + 1
        elif weapon2 == "L":
            print(f"Rock crushes Lizard! {player1} wins this round!")
            score1 = score1 + 1
        else :      # weapon2 must be Scissors
            print(f"Rock crushes Scissors! {player1} wins this round!")
            score1 = score1 + 1
            
    elif weapon1 == "P" :    #   Player1 chooses Paper
        if weapon2 == "P" :
            print("Thou hast ended in a Draw!")
        elif weapon2 == "R" :
            print(f"Paper covers Rock! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "V" :
            print(f"Paper disprooves Spock! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "L":
            print(f"Lizard shreds Paper! {player2} wins this round!")
            score2 = score2 + 1
        else :
            print(f"Scissors cut Paper! {player2} wins this round!")
            score2 = score2 + 1
            
    elif weapon1 == "L":    #   Player1 chooses Lizard
        if weapon2 == "L":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "V":
            print(f"Lizard poisons Spock! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "P":
            print(f"Lizard eats Paper! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "R":
            print(f"Rock crushes Lizard! {player2} wins this round!")
            score2 = score2 + 1
        else:
            print(f"Scissors decapitate Lizard! {player2} wins this round!")
            score2 = score2 + 1
            
    elif weapon1 == "V":    #   Player1 chooses Spock
        if weapon2 == "V":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "S":
            print(f"Spock somthing Scissors! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "R":
            print(f"Spock vapourizes Rock with his phaser! {player1} wins this round!")
            score1 = score1 + 1
        elif weapon2 == "L":
            print(f"Lizard poisons Spock! {player2} wins this round!")
            score2 = score2 + 1
        else:
            print(f"Paper disproves Spock! {player2} wins this round!")
            score2 = score2 + 1

    else:           # weapon1 must be Scissors
        if weapon2 == "S" :
            print("Thou hast ended in a Draw!")
        elif weapon2 == "R" :
            print(f"Rock breaks Scissors! {player2} wins this round!")
            score2 = score2 + 1
        else :      # weapon2 must be Paper
            print(f"Scissors cut Paper! {player1} wins this round!")
            score1 = score1 + 1

    print(f"""
    {player1} hath scored {score1} points.
    {player2} hath scored {score2} points.
    """)

    if score1 > score2:
        print(f"{player1} wins the duel!")
    elif score2 > score1:
        print(f"{player2} wins the duel!")
    else:
        print("The duel ends in a draw!")

    # == Play again?
    ask = input("Would thoust like another round? : ")
    if ask != "Y": isPlaying = False

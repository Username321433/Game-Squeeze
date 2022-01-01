import random, sys

print('---Sqeeze---\n')

tries = 0
hs = 0
current_num = 5
current_score = 0
while True:

    print("Number of Tries:", tries, "High Score:", hs, "\n")
    print("Current Number:", current_num)

    if current_score > hs:
        hs = current_score
        
    if current_num >= 10 or current_num <= 0:
        print("You lost!")
        tries = tries + 1
        current_num = 5
        current_score = 0
        continue

    print("Enter 1, 2, 3, or E to exit the game")
    while True:
        player_move = input()
        if player_move == "E":
            sys.exit()
        elif player_move == "1":
            print("You chose 1")
            break
        elif player_move == "2":
            print("You chose 2")
            break
        elif player_move == "3":
            print("You chose 3")
            break
        else:
            print("Please enter a valid value")
            continue

    
    player_move = int(player_move)
    
    pos_neg = random.randint(1,2)

    if pos_neg == 1:
        print("+ \n")
        current_num = current_num + player_move
    else:
        print("- \n")
        current_num = current_num - player_move
    
    current_score = current_score + 1
    
from data import *

def check_game_status(arena: list, who_shot: str):
    # Check if arena has any ships
    for i in range(10):
        for j in range(10):
            if arena[i][j] in ships:
                return None
    
    if who_shot == "player":
        print("Congratulations! You won.")
        return 0
    else:
        print("Computer won! Try again...")
        return 0
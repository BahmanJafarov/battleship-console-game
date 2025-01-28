from data import *

def check_hit(row: int, column: int, arena: list, who_shot: str):
    # If square has ship then replace it with 'X'
    if arena[row][column] in ships:
        arena[row][column] = 'X'
        if who_shot == "player":
            print("Result: Hit! You struck an enemy ship.")
        else:
            print("Result: Enemy struck your ship.")
    # If square has not ship then repalce it with 'O'
    else:
        # Additional logic for player not hitting the same place twice.
        if arena[row][column] == 'X':
            print("Don't shoot the same area twice!")
            return 

        # Empty square
        arena[row][column] = 'O'
        if who_shot == "player":
            print("Result: You missed!")
        else:
            print("Result: Miss! Your ships are safe.")

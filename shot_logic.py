import random

from check_hit_or_miss import check_hit
from data import *

def player_turn():
    while True:
        print("# Player's Turn")
        coor = input("Enter your shot coordinates (e.g., A5): ")

        # Inout validation.
        if coor == '':
            continue

        try:
            row, column = int(coor[1:]), coor[0].upper()
        except:
            print('Wrong coordinates! Enter again...')
            continue
        
        # Checking coordinates.
        if row not in rows or column not in columns.keys():
            print('Wrong coordinates! Enter again...')
            continue

        check_hit(row-1, int(columns[column]), arena_computer, "player")
        print()
        break


def computer_turn():
    print("#Computer's Turn")
    row, column = computer_shot_logic()
    print(f"Computer fires at coordinate {coords[column]}{row+1}...")
    check_hit(row, column, arena_player, "computer")
    print()

def computer_shot_logic():
    while True:
        row = random.randint(0, 9)
        column = random.randint(0, 9)

        # Don't hit the same area twice.
        if arena_player[row][column] in ('X', 'O'):
            continue
        else:
            return row, column
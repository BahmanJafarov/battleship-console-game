import random

from data import *
from board import *


# -----------------------------------------------------------------------------
def place_random_ships(arena):
    # Logic for placing the ships
    for ship in ships.keys():
        while True:

            isOverlapping = False
            # Randomly choose which side to place ships.
            index = random.randint(0,1)
            side = ['vertical', 'horizontal']

            # Generate indexes.
            # If Ship is VERTICAL.
            if side[index] == "vertical":
                # Start point
                column = random.randint(0, 9)
                row = random.randint(0, 10-ships[ship])

                # Check if it is overlapping
                for i in range(row, row+ships[ship]):
                    if arena[i][column] != '~':
                        isOverlapping = True
                        break
                
                # If overlapping then continue on While loop and generate another indexes.
                if isOverlapping: 
                    continue

                # Place the ships
                for i in range(row, row+ships[ship]):
                    arena[i][column] = ship

                # Break out of While loop to place other ships.
                break

            # IF Ship is Horizontal.
            else:
                # Start point
                row = random.randint(0, 9)
                column = random.randint(0, 10-ships[ship])

                # Check if it is overlapping
                for i in range(column, column+ships[ship]):
                    if arena[row][i] != '~':
                        isOverlapping = True
                        break
                
                # If overlapping then continue on While loop and generate another indexes.
                if isOverlapping: 
                    continue

                # Place the ships
                for i in range(column, column+ships[ship]):
                    arena[row][i] = ship
                
                # Break out of While loop to place other ships.
                break


# -----------------------------------------------------------------------------
def manual_ship_placement(arena_player):
    show_board_for_manual_placement()

    for ship in ships.keys():
        while True:

            # User Input Validation
            user_input = input(f"Enter coordinates for {ship}-{ship_names[ship]}-{ships[ship]} (e.g., 'A5 H' (H or V)): ")

            if user_input == '':
                print('Wrong coordinates! Enter again...')
                continue
            
            try:
                coor, side = user_input.split()
                row, column = int(coor[1:3]), coor[0].upper()
            except:
                print('Wrong coordinates! Enter again...')
                continue

            # Checking coordinates.
            if row not in rows or column not in columns.keys() or side.upper() not in ('H', 'V'):
                print('Wrong coordinates! Enter again...')
                continue

            # Get column number
            column = columns[column]

            # -1 for list indexing
            row -= 1

            side = side.upper()

            # Checking to not get out of range on board
            if side == "V" and row > (10-ships[ship]):
                print('Wrong coordinates! Enter again...')
                continue

            # Checking to not get out of range on board
            if side == "H" and column > (10-ships[ship]):
                print('Wrong coordinates! Enter again...')
                continue

            isOverlapping = False

            # If Ship is VERTICAL.
            if side.upper() == "V":

                # Check if it is overlapping
                for i in range(row, row+ships[ship]):
                    if arena_player[i][column] != '~':
                        isOverlapping = True
                        break
                
                # If overlapping then continue on While loop and generate another coordinates.
                if isOverlapping: 
                    print('Wrong coordinates! Overlapping! Enter again...')
                    continue

                # Place the ships
                for i in range(row, row+ships[ship]):
                    arena_player[i][column] = ship

                # Show board
                show_board_for_manual_placement()

                # Break out of While loop to place other ships.
                break

            # IF Ship is Horizontal.
            else:

                # Check if it is overlapping
                for i in range(column, column+ships[ship]):
                    if arena_player[row][i] != '~':
                        isOverlapping = True
                        break
                
                # If overlapping then continue on While loop and generate another coordinates.
                if isOverlapping: 
                    print('Wrong coordinates! Overlapping! Enter again...')
                    continue

                # Place the ships
                for i in range(column, column+ships[ship]):
                    arena_player[row][i] = ship

                # Show board
                show_board_for_manual_placement()

                # Break out of While loop to place other ships.
                break
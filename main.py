from board import *
from arena import *
from shot_logic import *
from status import *
from ship_placement import *

# =============================================================================
# ---------- MAIN LOGIC -------------------------------------------------------
# =============================================================================

print('Welcome to the game!')

# Get input from player (MANUAL or RANDOM placement).
while True:
    placement = input("Would you like 'MANUAL' or 'RANDOM' placement (M or R): ")
    if placement.upper() in ('M', 'R'):
        break
    else:
        print("Wrong choice!")

# Create arena for both players.
create_arena(arena_player, arena_computer, arena_computer_hidden)

# Place player ships.
if placement.upper() == 'M':
    manual_ship_placement(arena_player)
else:
    place_random_ships(arena_player)

# Place computer ships.
place_random_ships(arena_computer)

while True:
    show_board()

    player_turn()
    status = check_game_status(arena_computer, "player")
    if status is not None:
        break

    computer_turn()
    status = check_game_status(arena_player, "computer")
    if status is not None:
        break
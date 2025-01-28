from data import *

# -----------------------------------------------------------------------------
def show_board():

    update_computer_board()

    # # Test Computer Board
    # print("================== PLAYER'S BOARD ===================    =================== TARGET BOARD ====================")
    # print("  ", keys, "\t", "  ", keys)
    # for i in range(10):
    #     print(f"{i+1:2}", arena_player[i], "\t", f"{i+1:2}", arena_computer[i])

    print("\n================== PLAYER'S BOARD ===================    =================== TARGET BOARD ====================")
    print("  ", keys, "\t", "  ", keys)
    for i in range(10):
        print(f"{i+1:2}", arena_player[i], "\t", f"{i+1:2}", arena_computer_hidden[i])

    show_legend()


# -----------------------------------------------------------------------------
def update_computer_board():
    for i in range(10):
        for j in range(10):
            # Only show 'X' and 'O'.
            if arena_computer[i][j] in ('X', 'O'):
                arena_computer_hidden[i][j] = arena_computer[i][j]


# -----------------------------------------------------------------------------
def show_board_for_manual_placement():
    print("================== PLAYER'S BOARD =================== ")
    print("  ", keys)
    for i in range(10):
        print(f"{i+1:2}", arena_player[i])


# -----------------------------------------------------------------------------
def show_legend():
    print("\nLegend:")
    print("Your ships:\tShots:")
    print("C: Carrier\t~: Unknown")
    print("B: Battleship\tO: Miss")
    print("R: Cruiser\tX: Hit")
    print("S: Submarine")
    print("D: Destroyer\n")
def create_arena(arena_player, arena_computer, arena_computer_hidden):
    for _ in range(10):
        row_p = []
        row_c = []
        row_ch = []
        for _ in range(10):
            row_p.append('~')
            row_c.append('~')
            row_ch.append('~')
        arena_player.append(row_p)
        arena_computer.append(row_c)
        arena_computer_hidden.append(row_ch)
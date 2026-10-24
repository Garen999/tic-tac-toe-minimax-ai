#creates board
def create_board():
    #return [" " for _ in range(9)]
    return ["X","O","X","O","X"," "," ","O"," "]

#displays board in terminal
def display_board(grid):
    for i in range (0,9,3):
        print(grid[i],grid[i+1],grid[i+2])
    print("------------------------------")

#checks valid moves
def get_valid_moves(grid):
    return [i for i, space in enumerate(grid) if space == " "]

#makes move
def make_move(grid,valid_moves,symbol):
    while True:
        move = int(input(f"{symbol}, Choose a Space: "))
        if move in valid_moves:
            break
    grid[move] = symbol
    return grid

#checks the winner of game
def check_winner(grid,symbol):
    player_spaces = [True if space == symbol else False for space in grid]

    #checks horizontal rows
    for i in range (0,9,3):
        if all([player_spaces[i],player_spaces[i+1],player_spaces[i+2]]):
            return True

    #checks vertical rows
    for i in range (3):
        if all([player_spaces[i],player_spaces[i+3],player_spaces[i+6]]):
            return True

    #checks diagonal rows
    if all([player_spaces[0],player_spaces[4],player_spaces[8]]):
        return True
    elif all([player_spaces[2],player_spaces[4],player_spaces[6]]):
        return True

    return False

#checks game outcome
def win_condition(grid,is_winner):
    if is_winner:
        return False
    elif " " not in grid:
        print("It is a Draw")
        return False
    return True

#carries out a player's turn
def player_turn(grid,symbol):
    valid_moves = get_valid_moves(grid)
    grid = make_move(grid,valid_moves,symbol)
    display_board(grid)

    is_winner = check_winner(grid,symbol)
    if is_winner:
        print(f"{symbol} wins")

    running = win_condition(grid,is_winner)
    return grid,running

#gets following board states
def get_next_states(grid,symbol):
    new_valid_moves = get_valid_moves(grid)

    for valid_move in new_valid_moves:
        new_grid = grid.copy()
        new_grid[valid_move] = symbol

        display_board(new_grid)

        is_winner = check_winner(new_grid,symbol)
        if is_winner:
            print(f"{symbol} wins")
            print("------------------------------")
        elif not get_valid_moves(new_grid):
            print("Done")
        else:
            get_next_states(new_grid,"O" if symbol == "X" else "X")

#initialsing board
grid = create_board()
running = True
current_player = "X"

display_board(grid)

get_next_states(grid,current_player)

#main loop
# while running:

#     grid,running = player_turn(grid,current_player)

#     if not running:
#         break

#     current_player = "O" if current_player == "X" else "X"
    

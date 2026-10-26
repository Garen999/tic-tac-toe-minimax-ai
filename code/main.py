#creates board
def create_board():
    return [" " for _ in range(9)]

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
        move = int(input("Choose a Space: "))
        print("------------------------------")
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
    
    if symbol == "X":
        grid = make_move(grid,valid_moves,"X")
    else:
        grid[get_best_move(grid)] = "O"

    display_board(grid)

    is_winner = check_winner(grid,symbol)
    if is_winner:
        print(f"{symbol} wins")

    running = win_condition(grid,is_winner)
    return grid,running

#gets the following grid states
def get_next_states(grid,symbol):
    grid_states = {}
    valid_moves = get_valid_moves(grid)

    for valid_move in valid_moves:
        new_grid = grid.copy()
        new_grid[valid_move] = symbol
        grid_states.update({valid_move: new_grid})

    return grid_states

#minimax algorithim
def minimax(grid,symbol):
    scores = []
    is_cross_winner = check_winner(grid,"X")
    is_nought_winner = check_winner(grid,"O")
    
    if is_cross_winner:
        return -1
    elif is_nought_winner:
        return 1
    elif " " not in grid:
        return 0
    else:
        for grid_state in get_next_states(grid,symbol).values():
            scores.append(minimax(grid_state,"O" if symbol == "X" else "X"))
        if symbol == "X":
            return min(scores)
        else:
            return max(scores)
        
#chooses the best move for the bot to play
def get_best_move(grid):
    grid_state_scores = {}

    for move, grid in get_next_states(grid,"O").items():
        grid_state_scores.update({move: minimax(grid,"X")})
        
    return max(grid_state_scores, key=grid_state_scores.get)

#initialsing board
grid = create_board()
running = True
current_player = "X"
display_board(grid)

#main loop
while running:

    grid,running = player_turn(grid,current_player)

    if not running:
        break

    current_player = "O" if current_player == "X" else "X"
    

import game_board as gb
import numpy as np
import pandas as pd
import math

SQUID_TILE = 'XX'
EMPTY_TILE = '--'

# Get 2d coordinate from single int
def extrapolate_2d_coord(cell_num):
    cell_num -= 1
    row = int(np.floor(cell_num / 8))
    column = cell_num % 8
    return [row, column]

# Loops until a valid cell is chosen
def get_input(player_game_board):
    while True:
        cell_num = input("Enter cell number: ")
        try:
            cell_num = int(cell_num)
            if cell_num <= 64 and cell_num > 0:
                cell = extrapolate_2d_coord(cell_num)
                if player_game_board[cell[0], cell[1]] == EMPTY_TILE or player_game_board[cell[0], cell[1]] == SQUID_TILE:
                    print("Cell is not empty. Try again (1 - 64): ")
                else:
                    return cell
            else:
                print("Invalid cell number. Try again (1 - 64): ")
        except ValueError:
            print("Please input a number 1 - 64.")
    
# Update game board to display either a hit or a miss - assumes valid input    
def update_board(player_game_board, hidden_game_board, target_cell):
    
    if str(hidden_game_board[target_cell[0], target_cell[1]]) == ' ':
        player_game_board[target_cell[0], target_cell[1]] = EMPTY_TILE
        print("MISS!")
    else:
        player_game_board[target_cell[0], target_cell[1]] = SQUID_TILE
        print("HIT!")


# Update the boolean value for a squid cell when the player hits
def update_squid_array(target_cell, squid_array, squids_killed):
    for squid in squid_array:
        for cell in squid:
            if cell[0] == target_cell:
                cell[1] = True
                if check_kill(squid) == True:
                    squids_killed.append(1)

# Check each boolean value in each squid cell to see if hes dead
def check_kill(squid):
    for cell in squid:
        if cell[1] == False:
            return False
    print("Killed squid of size:", len(squid))
    return True

def fix_row_one(pb):
    for i in range(8):
        pb[0][i] = "0" + str(i + 1)
    pb[1][0] = "09"
    return pb

def game_loop():
    num_squids = 3
    game_board = gb.generate_game_board(num_squids)
    squid_array = game_board[1]
    hidden_game_board = game_board[0]    
    player_game_board = np.arange(1, 65).reshape((8,8)).astype(str)
    player_game_board = fix_row_one(player_game_board)
    squids_killed = []
    starting_cannonballs = 24
    cannonballs = 24

    #print(hidden_game_board)

    while True:
        print("Squids Killed: ", len(squids_killed))
        print("Cannonballs Remaining: ", cannonballs, '\n')
        print(player_game_board, '\n')

        # Function ensures valid input
        target_cell = get_input(player_game_board)
        cannonballs -= 1
        print('\n', '\n')

        update_board(player_game_board, hidden_game_board, target_cell)
        update_squid_array(target_cell, squid_array, squids_killed)

        print('\n')

        if len(squids_killed) == num_squids:
            print(hidden_game_board, '\n')
            print("Nice huntin' chub, ya win!", '\n')
            print("You used:", starting_cannonballs - cannonballs, " out of 24 cannonballs")
            break

        if cannonballs == 0:
            print(hidden_game_board, '\n')
            print("Argg, plunder ye! Ya lose!", '\n')
            print("You used: ", starting_cannonballs - cannonballs, " out of ", starting_cannonballs, " cannonballs")
            print("You got: ", len(squids_killed), " out of ", num_squids, " squids")
            break

        


game_loop()
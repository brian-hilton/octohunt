import numpy as np
import pandas as pd

def about():
    """
    Goal: Generate "sploosh kaboom" maps. 
    Sploosh kaboom is a minigame from The Legend of Zelda Wind Waker that is akin to battleship.
    There is an 8x8 grid with three hidden 'octos' that must be bombed by the player.
    The three octos are two tiles, three tiles, and four tiles long.
    Octos can be adjacent to one another but cannot overlap or extend beyond the 8x8 grid.
    The player has 24 cannonballs to hunt all three octos. They can enter a coordinate and
    fire a cannonball to check a tile for an octo. If they 'hit', the visually empty cell will populate with a '*'
    character to indicate part of an octo was hit. With part of the octo revealed, they can check adjacent tiles until 
    the octo has been fully bombed. Uncovered tiles cannot be bombed again.
    If a player shoots a tile with no octos, an 'X' will appear to indicate a miss. They cannot choose this coordinate again.
    The game ends when a player either bombs all the octos (win) or has no more cannonballs (lose).    
    """
    ignore = 1

def get_random_coordinate():
    # Generate random number to represent position on board (one of the 64 tiles)
    # Indexing starts at 0. The upper bound is 64 (exclusive) so coordinates range from (0,0) to (7,7) which would represent positions 0 and 64, respectively.
    # Extrapolates 2-dimensional coordinate from single integer
    #print('Position: ', ran_num, '\n')
    ran_num = np.random.randint(0, high=64)    
    row = int(np.floor(ran_num / 8))
    column = ran_num % 8
    coord = [row, column]
    return coord

def get_random_coordinate2():
    # More straight forward method to determine coordinate.
    x = np.random.randint(0, high=64)
    y = np.random.randint(0, high=64)
    coord = [x,y]
    return coord

def get_random_direction():
    return(np.random.randint(0, high=4))

def generate_squid(game_board, squid_length, squid_array):
    # Get random coordinate and coordinate to draw squid
    collision = False
    coord = get_random_coordinate()
    direction = get_random_direction() # 0 = Down, 1 = Left, 2 = Up, 3 = Right
    debug = False
    
    # Validate squid can be drawn for all direcions and does not collide with existing squid. Recall function if squid cannot be drawn at coordinate
    if direction == 0:
        if coord[0] - 1 + squid_length <= 7:
            for i in range(squid_length):
                if game_board[coord[0] + i, coord[1]] != ' ':
                    collision = True

            if collision == False:
                squid = []
                if debug:
                    print(coord, 'down', '\n')
                for i in range(squid_length):
                    game_board[coord[0] + i, coord[1]] = 'V'
                    squid.append([[coord[0] + i, coord[1]], False])  
                squid_array.append(squid)
            else:
                generate_squid(game_board, squid_length, squid_array)     
        else:
            generate_squid(game_board, squid_length, squid_array)
    


    if direction == 1:
        if coord[1] + 1 - squid_length >= 0:
            for i in range(squid_length):
                if game_board[coord[0], coord[1] - i] != ' ':
                    collision = True

            if collision == False:
                squid = []
                if debug:
                    print(coord, 'left', '\n')
                for i in range(squid_length):
                    game_board[coord[0], coord[1] - i] = '<'
                    squid.append([[coord[0], coord[1] - i], False])
                squid_array.append(squid)
            else:
                generate_squid(game_board, squid_length, squid_array) 
        else:
            generate_squid(game_board, squid_length, squid_array)
    


    if direction == 2:
        if coord[0] + 1 - squid_length >= 0:
            for i in range(squid_length):
                if game_board[coord[0] - i, coord[1]] != ' ':
                    collision = True

            if collision == False:
                squid = []
                if debug:
                    print(coord, 'up', '\n')
                for i in range(squid_length):
                    game_board[coord[0] - i, coord[1]] = '^'
                    squid.append([[coord[0] - i, coord[1]], False])
                squid_array.append(squid)
            else:
                generate_squid(game_board, squid_length, squid_array) 
        else:
            generate_squid(game_board, squid_length, squid_array)
    


    if direction == 3:
        if coord[1] - 1 + squid_length <= 7:
            for i in range(squid_length):
                if game_board[coord[0], coord[1] + i] != ' ':
                    collision = True
            
            if collision == False:
                squid = []
                if debug:
                    print(coord, 'right', '\n')
                for i in range(squid_length):
                    game_board[coord[0], coord[1] + i] = '>'
                    squid.append([[coord[0], coord[1] + i], False])
                squid_array.append(squid)
            else:
                generate_squid(game_board, squid_length, squid_array) 
        else:
            generate_squid(game_board, squid_length, squid_array)  
    
    return game_board

def generate_game_board(num_squids):
    # Generate empty game board; fill with 'O's
    game_board = np.full((8,8), fill_value=' ', dtype=str)
    squid_array = []
    for i in range(num_squids):
        generate_squid(game_board, i + 2, squid_array)
    return (game_board, squid_array)


# board = np.full((8,8), fill_value='o', dtype=str)
# board = generate_squid(board, 2)
# print(board)
# board = generate_squid(board, 3)
# print(board)

# game = generate_game_board(3)
# print(game[0], '\n', game[1])
# squid_array = game[1]
# print(squid_array[2])




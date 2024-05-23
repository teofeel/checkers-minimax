from .constants import *
from .hashmap import HashMap
import copy
import os

#boards = HashMap()
boards = {}

def heuristic(board):
    BASIC_PIECE_SCORE = 50

    if not board.MUST_ATTACK:
        BASIC_PIECE_SCORE = 65

    ADVANCED_PIECE_SCORE = 15
    QUEEN_WEIGHT = 15
    ATTACK_WEIGHT = 25
    CAN_BE_CAPTURED_WEIGHT = -30
    CORNER_WEIGHT = -1
    WALL_WEIGHT = -0.5
    POSSIBLE_MOVES_WEUGHT = 15

    black_basic_score           = board.black_pieces_left                       * BASIC_PIECE_SCORE
    black_advanced_piece_score  = board.get_advanced_pieces(BLACK)              * ADVANCED_PIECE_SCORE
    black_queen_score           = board.black_piece_queens                      * QUEEN_WEIGHT
    black_attack_position_score = board.get_num_pieces_attack_positions(BLACK)  * ATTACK_WEIGHT
    black_can_be_captured_score = board.get_pieces_can_be_captured(BLACK)       * CAN_BE_CAPTURED_WEIGHT
    black_corner_score          = board.get_pieces_corner(BLACK)                * CORNER_WEIGHT
    black_wall_score            = board.get_pieces_wall(BLACK)                  * WALL_WEIGHT
    black_possible_moves_score  = len(board.get_pieces_movement_algo(BLACK))    * POSSIBLE_MOVES_WEUGHT

    black_score = (black_basic_score+ black_advanced_piece_score + black_queen_score +  black_attack_position_score + 
                   black_can_be_captured_score + black_corner_score + black_wall_score + black_possible_moves_score)

    red_basic_score             = board.red_pieces_left                         * BASIC_PIECE_SCORE
    red_advanced_piece_score    = board.get_advanced_pieces(RED)                * ADVANCED_PIECE_SCORE
    req_queen_score             = board.red_piece_queens                        * QUEEN_WEIGHT
    red_attack_position_score   = board.get_num_pieces_attack_positions(RED)    * ATTACK_WEIGHT
    red_can_be_captured_score   = board.get_pieces_can_be_captured(RED)         * CAN_BE_CAPTURED_WEIGHT
    red_corner_score            = board.get_pieces_corner(RED)                  * CORNER_WEIGHT
    red_wall_score              = board.get_pieces_wall(RED)                    * WALL_WEIGHT
    red_possible_moves_score    = len(board.get_pieces_movement_algo(RED))      * POSSIBLE_MOVES_WEUGHT

    red_score = (red_basic_score + red_advanced_piece_score + req_queen_score + red_attack_position_score + 
                 red_can_be_captured_score + red_corner_score + red_wall_score + red_possible_moves_score)

    return red_score - black_score

def extract_data(file):
    for line in file.readlines():
        data = line.split('\n')[0]
        board = data.split('[')[0]

        move = data.split('[')[1].split(']')[0].replace('(','').replace(')','')
                
        nums = move.split(', ')
        move_from = tuple(map(int, [nums[0], nums[1]]))
        move_to = tuple(map(int, [nums[2], nums[3]]))

        boards[board] = [move_from, move_to]

def load_boards(must_attack):
    global boards

    if must_attack:

        if os.stat('must_attack_boards.txt').st_size==0:
            return
        
        with open('must_attack_boards.txt','r') as file:
            extract_data(file)
    else:
        if os.stat('boards.txt').st_size==0:
            return
        
        with open('boards.txt','r') as file:
            extract_data(file)
            

def save_boards(must_attack):
    if must_attack:
        with open('must_attack_boards.txt','w') as file:
            for board in boards:
                file.write(str(board)+str(boards[board])+'\n')

    else:
        with open('boards.txt','w') as file:
            for board in boards:
                file.write(str(board)+str(boards[board])+'\n')


def minimax(board, depth, maximizer, alpha, beta, hash_map):
    if depth == 0:
        return heuristic(board)
    
    if maximizer == RED: 
        max_value = float('-inf')

        for move_suggest in board.get_pieces_movement_algo(maximizer):
            possible_piece = move_suggest[0]
            move = move_suggest[1]

            board_temp = copy.deepcopy(board)
            board_temp.move_piece([move_suggest[1]], possible_piece[1], possible_piece[0], move[1], move[0])    

            value = minimax(board_temp, depth-1, BLACK, alpha, beta, hash_map)
            
            if value >= max_value:
                max_value=value

                if depth>2:
                    hash_map[max_value] = move_suggest
            
            alpha = max(alpha, value)

            if beta <= alpha:
                break


        return max_value 

    else:
        min_value = float('inf')

        for move_suggest in board.get_pieces_movement_algo(maximizer):
            possible_piece = move_suggest[0]
            move = move_suggest[1]

            board_temp = copy.deepcopy(board)
            board_temp.move_piece([move_suggest[1]], possible_piece[1], possible_piece[0], move[1], move[0])

            value = minimax(board_temp, depth-1, RED, alpha, beta, hash_map)

            if value <= min_value:
                min_value = value

            beta = min(beta, value)
            if beta <= alpha:
                break

        return min_value


def make_move(board, player, depth):
    hash_map = HashMap()

    if str(board) in boards and boards[str(board)]!=None:
        return boards[str(board)]

    board_temp = copy.deepcopy(board)
    
    move_value = minimax(board_temp, depth, player, float('-inf'), float('inf'), hash_map)

    if board.red_pieces_left + board.black_pieces_left>7 and hash_map[move_value]!=None:
        boards[str(board)] = hash_map[move_value]

    return hash_map[move_value]
            






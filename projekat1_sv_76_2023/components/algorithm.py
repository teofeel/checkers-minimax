from .constants import *
from .hashmap import HashMap

def heuristic(board):
    QUEEN_WEIGHT = 2
    ATTACK_WEIGHT = 3
    CORNER_WEIGHT = 1.5
    WALL_WEIGHT = 1.2


    black_queen_score = board.black_piece_queens*QUEEN_WEIGHT
    black_attack_position_score = board.get_num_pieces_attack_positions(BLACK)*ATTACK_WEIGHT
    black_corner_score = board.get_pieces_corner(BLACK)*CORNER_WEIGHT
    black_wall_score = board.get_pieces_wall(BLACK)*WALL_WEIGHT

    black_score = (board.black_pieces_left - (board.black_piece_queens +  board.get_num_pieces_attack_positions(BLACK) + board.get_pieces_corner(BLACK) +  board.get_pieces_wall(BLACK)) + 
                    black_queen_score +  black_attack_position_score + black_corner_score + black_wall_score)
    
    
    req_queen_score = board.red_piece_queens*QUEEN_WEIGHT
    red_attack_position_score = board.get_num_pieces_attack_positions(RED)*ATTACK_WEIGHT
    red_corner_score = board.get_pieces_corner(RED)*CORNER_WEIGHT
    red_wall_score = board.get_pieces_wall(RED)*WALL_WEIGHT

    red_score = (board.red_pieces_left - (board.red_piece_queens + board.get_num_pieces_attack_positions(RED) + board.get_pieces_corner(RED) + board.get_pieces_wall(RED)) + 
                    req_queen_score + red_attack_position_score + red_corner_score + red_wall_score)


    return black_score, red_score

    

def minimax(board, depth, maximizer, alpha, beta, value):
    print(board.get_pieces_wall(BLACK))
    



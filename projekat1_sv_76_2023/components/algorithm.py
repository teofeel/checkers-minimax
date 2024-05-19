from .constants import *
from .hashmap import HashMap
import copy

def heuristic(board):
    QUEEN_WEIGHT = 1.8
    ATTACK_WEIGHT = 2
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



def minimax(board, depth, maximizer, alpha, beta, hash_map):
    if depth == 0:
        heuristic_score = heuristic(board)
        black_score = heuristic_score[0]
        red_score = heuristic_score[1]
        return black_score-red_score
    
    if maximizer == RED: #Maximizer is 
        max_value = float('-inf')

        for suggested_piece in board.draw_suggested_pieces_board(maximizer):
            piece_row, piece_col = suggested_piece[0], suggested_piece[1]

            board_temp = copy.deepcopy(board)
            possibles_moves = board_temp.selected_piece(piece_col, piece_row, maximizer)

            for possible_move in possibles_moves:
                possible_move_row, possible_move_col = possible_move[0], possible_move[1]
                
                board_temp1 = copy.deepcopy(board_temp)

                board_temp1.move_piece(possibles_moves, piece_col, piece_row, possible_move_col, possible_move_row)
                value = minimax(board_temp, depth-1, BLACK, alpha, beta, hash_map)

                if max_value<value:
                    max_value = value
                    

                if max_value<=value and depth>=1:
                    hash_map[max_value] = [suggested_piece, [possible_move]]   

                alpha = max(alpha, value)   

                if beta<=alpha:
                    break


        return max_value 

    else:
        min_value = float('inf')
        

        for suggested_piece in board.draw_suggested_pieces_board(maximizer):
            piece_row, piece_col = suggested_piece[0], suggested_piece[1]

            board_temp = copy.deepcopy(board)
            possibles_moves = board_temp.selected_piece(piece_col, piece_row, maximizer)

            for possible_move in possibles_moves:
                possible_move_row, possible_move_col = possible_move[0], possible_move[1]
                
                board_temp1 = copy.deepcopy(board_temp)

                board_temp1.move_piece(possibles_moves, piece_col, piece_row, possible_move_col, possible_move_row)
                value = minimax(board_temp, depth-1, RED, alpha, beta, hash_map)

                if min_value>value:
                    min_value = value
                    

                if min_value>=value and depth>=1:
                    hash_map[min_value] = [suggested_piece, [possible_move]]  

                alpha = max(alpha, value)   
                
                if beta<=alpha:
                    break

        return min_value

    
def test(hash_map):
    hash_map[1]=1

def make_move(board, player, depth):
    hash_map = HashMap()

    board_temp = copy.deepcopy(board)

    move_value = minimax(board_temp, depth, player, 0, 0, hash_map)

    
    

    return hash_map[move_value]
            






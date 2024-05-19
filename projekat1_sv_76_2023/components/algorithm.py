from .constants import *
from .hashmap import HashMap
import copy

def heuristic(board):
    BASIC_PIECE_SCORE = 20
    ADVANCED_PIECE_SCORE = 15
    QUEEN_WEIGHT = 5
    ATTACK_WEIGHT = 15
    CAN_BE_CAPTURED_WEIGHT = -15
    CORNER_WEIGHT = -1
    WALL_WEIGHT = -0.5


    black_basic_score           = board.black_pieces_left                       * BASIC_PIECE_SCORE
    black_advanced_piece_score  = board.get_advanced_pieces(BLACK)              * ADVANCED_PIECE_SCORE
    black_queen_score           = board.black_piece_queens                      * QUEEN_WEIGHT
    black_attack_position_score = board.get_num_pieces_attack_positions(BLACK)  * ATTACK_WEIGHT
    black_can_be_captured_score = board.get_pieces_can_be_captured(BLACK)       * CAN_BE_CAPTURED_WEIGHT
    black_corner_score          = board.get_pieces_corner(BLACK)                * CORNER_WEIGHT
    black_wall_score            = board.get_pieces_wall(BLACK)                  * WALL_WEIGHT

    black_score = black_basic_score+ black_advanced_piece_score + black_queen_score +  black_attack_position_score+black_can_be_captured_score + black_corner_score + black_wall_score

    red_basic_score             = board.red_pieces_left                         * BASIC_PIECE_SCORE
    red_advanced_piece_score    = board.get_advanced_pieces(RED)                * ADVANCED_PIECE_SCORE
    req_queen_score             = board.red_piece_queens                        * QUEEN_WEIGHT
    red_attack_position_score   = board.get_num_pieces_attack_positions(RED)    * ATTACK_WEIGHT
    red_can_be_captured_score   = board.get_pieces_can_be_captured(RED)         * CAN_BE_CAPTURED_WEIGHT
    red_corner_score            = board.get_pieces_corner(RED)                  * CORNER_WEIGHT
    red_wall_score              = board.get_pieces_wall(RED)                    * WALL_WEIGHT

    red_score = red_basic_score + red_advanced_piece_score + req_queen_score + red_attack_position_score+red_can_be_captured_score + red_corner_score + red_wall_score


    return red_score - black_score

def get_moves(board, player):
    moves = []
    boards = []

    for row in range(ROWS):
        for col in range(COLS):
            piece = board.board[row][col]

            if piece!=0 and piece.color == player and not board.MUST_ATTACK:
                if not board.out_of_bounds(row-1,col-1):
                    point1 = board.board[row-1][col-1]
                else: point1 = None

                if not board.out_of_bounds(row-1,col+1):
                    point2 = board.board[row-1][col+1]
                else: point2 = None

                if not board.out_of_bounds(row+1,col-1):
                    point3 = board.board[row+1][col-1]
                else: point3 = None

                if not board.out_of_bounds(row+1,col+1):
                    point4 = board.board[row+1][col+1]
                else: point4 = None

                if (point1 != None and point1 == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)

                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row-1][col-1] = piece_temp
                    

                    moves.append([[row,col],[row-1,col-1]])
                    boards.append(board_temp)

                if (point1 != None and point1 != 0 and point1.color!=player and not board.out_of_bounds(row-2, col-2) and board.board[row-2][col-2] == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)

                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row-2][col-2] = piece_temp

                    moves.append([[row,col],[row-2,col-2]])
                    boards.append(board_temp)

                if (point2 != None and point2 == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row-1][col+1] = piece_temp

                    moves.append([[row,col],[row-1,col+1]])
                    boards.append(board_temp)

                if (point2 != None and point2 != 0 and point2.color!=player and not board.out_of_bounds(row-2, col+2) and board.board[row-2][col+2] == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row-2][col+2] = piece_temp

                    moves.append([[row,col],[row-2,col+2]])
                    boards.append(board_temp)

                if (point3 != None and point3 == 0) and (piece.direction==1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row+1][col-1] = piece_temp

                    moves.append([[row,col],[row+1,col-1]])
                    boards.append(board_temp)

                if (point3 != None and point3 != 0 and point3.color!=player and not board.out_of_bounds(row+2, col-2) and board.board[row+2][col-2] == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row+2][col-2] = piece_temp

                    moves.append([[row,col],[row+2,col-2]])
                    boards.append(board_temp)

                if (point4 != None and point4 == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row+1][col+1] = piece_temp

                    moves.append([[row,col],[row+1,col+1]])
                    boards.append(board_temp)

                if (point4 != None and point4 != 0 and point4.color!=player and not board.out_of_bounds(row+2, col+2) and board.board[row+2][col+2] == 0) and (piece.direction==-1 or piece.is_queen):
                    board_temp = copy.deepcopy(board)
                    piece_temp = board_temp.board[row][col]
                    board_temp.board[row][col] = 0
                    board_temp.board[row+2][col+2] = piece_temp

                    moves.append([[row,col],[row+2,col+2]])
                    boards.append(board_temp)
            else:
                pass

    return moves, boards        
        

def optimized_minimax(board, depth, maximizer, alpha, beta, hash_map):
    if depth == 0:
        return heuristic(board)
    
    if maximizer == RED: 
        max_value = float('-inf')

        moves, boards = get_moves(board, maximizer)
        
        for i in range(len(moves)):
            value = minimax(boards[i], depth-1, BLACK, alpha, beta, hash_map)

            if value>=max_value:
                max_value = value
                hash_map[max_value] = [moves[i][0], [moves[i][1]]]
            

            alpha = max(alpha, value)

            if beta<= alpha:
                break
        
        return max_value 

    else:
        min_value = float('inf')

        moves, boards = get_moves(board, maximizer)
        for i in range(len(moves)):
            value = minimax(boards[i], depth-1, RED, alpha, beta, hash_map)

            if min_value>=value:
                min_value = value
                hash_map[min_value] = [moves[i][0], [moves[i][1]]]

            beta = min(beta, value)

            if beta <= alpha:
                break

        return min_value
    
    

def minimax(board, depth, maximizer, alpha, beta, hash_map):
    if depth == 0:
        #print(heuristic(board))
        return heuristic(board)
    
    if maximizer == RED: 
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
                
                if max_value<=value and depth>2:
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
                    
                if min_value>=value and depth>2:
                    hash_map[min_value] = [suggested_piece, [possible_move]]  

                beta = min(beta, value)   
                
                if beta <= alpha:
                    break

        return min_value
    
def make_move(board, player, depth):
    hash_map = HashMap()

    board_temp = copy.deepcopy(board)

    move_value = minimax(board_temp, depth, player, float('-inf'), float('inf'), hash_map)

    return hash_map[move_value]
            






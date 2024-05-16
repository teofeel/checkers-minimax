import pygame
from .Piece import Piece
from .constants import *

class Board:
    def __init__(self):
        self.board=[]

        self.black_pieces_left = 12
        self.red_pieces_left = 12

        self.piece_selected = None

        self.black_piece_queens = 0
        self.red_piece_queens = 0

    def out_of_bounds(self, row, col):
        if(row>=0 and col>=0 and row<=7 and col<=7):
            return False
        return True

    def draw_positions(self, window):
        window.fill(DARK_BROWN)
        for col in range(COLS):
            for row in range(col%2, ROWS, 2):
                pygame.draw.rect(window, LIGHT_BROWN,(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))        
    def draw_pieces_board_beggining(self, window):
        for row in range(ROWS):
            self.board.append([])
            for column in range(COLS):
                if column % 2 == (row+1)%2:
                    if row<3:
                        self.board[row].append(Piece(row,column,RED))
                    elif row>4:
                        self.board[row].append(Piece(row,column,BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        for row in range(ROWS):
            self.board.append([])
            for column in range(COLS):
                piece = self.board[row][column]
                if piece!=0:
                    piece.draw_circle(window)

    def draw_pieces_board(self, window):
        for row in range(ROWS):
            for column in range(COLS):
                piece = self.board[row][column]
                if piece!=0:
                    piece.draw_circle(window)


    def check_draw_possible_move(self, row, column, window):
        if(not self.out_of_bounds(row,column) and self.board[row][column]==0):
            pygame.draw.rect(window, GREEN, (column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def selected_piece(self,window, position, player):
        position_col, position_row = position[0]//SQUARE_SIZE, position[1]//SQUARE_SIZE

        if(self.board[position_row][position_col]!=0 and self.board[position_row][position_col].color==player 
           and not self.board[position_row][position_col].is_queen):
            
            can_move_row = self.board[position_row][position_col].direction+position_row

            can_move_col1 = position_col+1
            can_move_col2 = position_col-1
            
            self.check_draw_possible_move(can_move_row, can_move_col1, window)
            self.check_draw_possible_move(can_move_row, can_move_col2, window)    
            pygame.display.update()

            possible_move1 = (can_move_row, can_move_col1)
            possible_move2 = (can_move_row, can_move_col2)
            
            return possible_move1, possible_move2
            
        elif(self.board[position_row][position_col]!=0 and self.board[position_row][position_col].color==player 
           and self.board[position_row][position_col].is_queen):
            pass

        else:
            return False


    def move_piece(self,window, possible_moves, piece_pos, move_pos):
        piece_col, piece_row = piece_pos[0]//SQUARE_SIZE, piece_pos[1]//SQUARE_SIZE
        move_col, move_row = move_pos[0]//SQUARE_SIZE, move_pos[1]//SQUARE_SIZE

        for move in possible_moves:
            possible_move_row = move[0]
            possible_move_col = move[1]
            
            if((not self.out_of_bounds(possible_move_row, possible_move_col)) and self.board[possible_move_row][possible_move_col]==0 
               and (possible_move_row==move_row and possible_move_col==move_col)):
                
                self.board[move_row][move_col] = self.board[piece_row][piece_col]
                self.board[move_row][move_col].column = move_col
                self.board[move_row][move_col].row = move_row

                self.board[piece_row][piece_col] = 0

                self.board[move_row][move_col].draw_circle(window)
                pygame.display.update()

                return True
            
            elif((self.out_of_bounds(possible_move_row, possible_move_col) or self.board[possible_move_row][possible_move_col]!=0 )
               and (possible_move_row==move_row and possible_move_col==move_col)):
                
                return False

    

        

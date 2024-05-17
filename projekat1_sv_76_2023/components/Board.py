import pygame
from .Piece import Piece
from .constants import *
import math

class Board:
    def __init__(self):
        self.board=[] # PREBACITI OVO U HASHMAPU

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



    def check_draw_possible_move(self, row, column, player, player_pos):
        player_pos_col, player_pos_row = player_pos

        if(not self.out_of_bounds(row,column) and self.board[row][column]==0):
            return row, column
        
        elif(not self.out_of_bounds(row, column) and self.board[row][column]!=0 and self.board[row][column].color!=player.color):
            ##### ovde greksa kad je kraljica ######
            if not player.is_queen:
                row_temp = row+player.direction
                if column-player_pos_col>0:
                    column_temp=column+abs(player.direction)
                elif column-player_pos_col<0:
                    column_temp=column-abs(player.direction)
            else:
                if row>player_pos_row:
                    row_temp = row+1
                else:
                    row_temp = row-1

                if column-player_pos_col>0:
                    column_temp=column+1
                elif column-player_pos_col<0:
                    column_temp=column-1

            if(not self.out_of_bounds(row_temp,column_temp) and self.board[row_temp][column_temp]==0):
                return row_temp, column_temp
        
        return None, None

        
    

    def get_pieces_attack_position(self, player_color):
        ######### NAPISATI OVO DNS ##############
        available_pieces = []

        for row in range(ROWS):
            for column in (COLS):
                pass

        
    def check_draw_possible_mustattack(self, player_pos_row, possible_move1_row, possible_move2_row):
        if MUST_ATTACK and possible_move1_row!=None and possible_move2_row!=None:
            if ((abs(player_pos_row-possible_move1_row)>1 or abs(player_pos_row-possible_move2_row)>1) and
                (abs(player_pos_row-possible_move1_row)==1 or abs(player_pos_row-possible_move2_row)==1)):
            
                if abs(player_pos_row-possible_move1_row)==1: possible_move1_row = None
                else: possible_move2_row = None
        
        return possible_move1_row, possible_move2_row
        

    def selected_piece(self,window, position_col, position_row, player):
        if(self.board[position_row][position_col]!=0 and self.board[position_row][position_col].color==player):
            possible_moves = []

            can_move_row = self.board[position_row][position_col].direction+position_row

            can_move_col1 = position_col+1
            can_move_col2 = position_col-1
            
            can_move_row1, can_move_col1 = self.check_draw_possible_move(can_move_row, can_move_col1, self.board[position_row][position_col], (position_col, position_row))
            can_move_row2, can_move_col2 = self.check_draw_possible_move(can_move_row, can_move_col2, self.board[position_row][position_col], (position_col, position_row))

            if self.board[position_row][position_col].is_queen:
                can_move_row_queen = self.board[position_row][position_col].direction*(-1)+position_row
                can_move_col1_queen = position_col+1
                can_move_col2_queen = position_col-1

                can_move_row3, can_move_col3 = self.check_draw_possible_move(can_move_row_queen, can_move_col1_queen, self.board[position_row][position_col], (position_col, position_row))
                can_move_row4, can_move_col4 = self.check_draw_possible_move(can_move_row_queen, can_move_col2_queen, self.board[position_row][position_col], (position_col, position_row))

            #can_move_row1, can_move_row2 = self.check_draw_possible_mustattack(position_row, can_move_row1, can_move_row2)
            
            if (can_move_row1!=None and can_move_col1!=None):
                possible_moves.append((can_move_row1, can_move_col1))
                pygame.draw.rect(window, GREEN, (can_move_col1 * SQUARE_SIZE, can_move_row1 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            if (can_move_row2!=None and can_move_col2!=None):
                possible_moves.append((can_move_row2, can_move_col2))
                pygame.draw.rect(window, GREEN, (can_move_col2 * SQUARE_SIZE, can_move_row2 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            if (self.board[position_row][position_col].is_queen and can_move_row3!=None and can_move_col3!=None):
                possible_moves.append((can_move_row3, can_move_col3))
                pygame.draw.rect(window, GREEN, (can_move_col3 * SQUARE_SIZE, can_move_row3 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            if (self.board[position_row][position_col].is_queen and can_move_row4!=None and can_move_col4!=None):
                possible_moves.append((can_move_row4, can_move_col4))
                pygame.draw.rect(window, GREEN, (can_move_col4 * SQUARE_SIZE, can_move_row4 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            pygame.display.update()

            return possible_moves
        else:
            return False

    def remove_piece(self, player, move_col, move_row, piece_col, piece_row):
        if move_row>piece_row:
            remove_piece_row = move_row-1
            if move_col>piece_col:
                remove_piece_col = move_col-1
            else:
                remove_piece_col = move_col+1
        else:
            remove_piece_row = piece_row-1
            if move_col>piece_col:
                remove_piece_col = move_col-1
            else:
                remove_piece_col = move_col+1

        piece_color = self.board[remove_piece_row][remove_piece_col].color
        piece_is_queen = self.board[remove_piece_row][remove_piece_col].is_queen
        self.board[remove_piece_row][remove_piece_col] = 0

        if piece_color == BLACK: self.black_pieces_left-=1
        else: self.red_pieces_left-=1

        if piece_is_queen:
            if piece_color == BLACK: self.black_piece_queens-=1
            else: self.red_piece_queens-=1       

    def move_piece(self,window, possible_moves, piece_col, piece_row, move_col, move_row):
        for move in possible_moves:
            possible_move_row = move[0]
            possible_move_col = move[1]
            
            if((not self.out_of_bounds(possible_move_row, possible_move_col)) and self.board[possible_move_row][possible_move_col]==0 
               and (possible_move_row==move_row and possible_move_col==move_col)):
                
                if abs(move_row-piece_row)==2:
                    self.remove_piece(self.board[piece_row][piece_col], move_col, move_row, piece_col, piece_row)
                
                self.board[move_row][move_col] = self.board[piece_row][piece_col]
                self.board[move_row][move_col].column = move_col
                self.board[move_row][move_col].row = move_row

                self.board[piece_row][piece_col] = 0

                self.board[move_row][move_col].draw_circle(window)
                pygame.display.update()

                ######## OVO PREGLEDATI ########
                if(self.board[move_row][move_col].color == BLACK and move_row==0):
                    self.board[move_row][move_col].is_queen = True
                elif(self.board[move_row][move_col].color == RED and move_row==ROWS-1):
                    self.board[move_row][move_col].is_queen = True
                ################################

                return True
            
            elif((self.out_of_bounds(possible_move_row, possible_move_col) or self.board[possible_move_row][possible_move_col]!=0 )
               and (possible_move_row==move_row and possible_move_col==move_col)):
                return False
            

    

        

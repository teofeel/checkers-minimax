import pygame
from .Piece import Piece
from .constants import *
from .hashmap import HashMap

class Board:
    def __init__(self):
        self._board=[] # PREBACITI OVO U HASHMAPU

        self._black_pieces_left = 12
        self._red_pieces_left = 12

        self._piece_selected = None

        self._black_piece_queens = 0
        self._red_piece_queens = 0

        self._MUST_ATTACK = False

    @property
    def board(self):
        return self._board
    @property
    def black_pieces_left(self):
        return self._black_pieces_left
    @property
    def red_pieces_left(self):
        return self._red_pieces_left
    @property
    def black_piece_queens(self):
        return self._black_piece_queens
    @property
    def red_piece_queens(self):
        return self._red_piece_queens
    @property
    def MUST_ATTACK(self):
        return self._MUST_ATTACK
    
    @board.setter
    def board(self, row, col, value):
        self._board[row][col] = value

    @board.setter
    def board(self, value):
        self._board = value

        self._black_pieces_left = 0
        self._red_pieces_left = 0
        self._red_piece_queens = 0
        self._black_piece_queens = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                if piece!=0:
                    if piece.color == BLACK:
                        self._black_pieces_left +=1

                    elif piece.color == RED:
                        self._red_pieces_left +=1

                    if piece.color == BLACK and piece.is_queen:
                        self._black_piece_queens += 1

                    elif piece.color == BLACK and piece.is_queen:
                        self._red_piece_queens += 1


    @black_pieces_left.setter
    def black_pieces_left(self, value):
        self._black_pieces_left = value

    @red_pieces_left.setter
    def red_pieces_left(self, value):
        self._red_pieces_left = value

    @MUST_ATTACK.setter
    def MUST_ATTACK(self, value):
        self._MUST_ATTACK = value
    

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
            self._board.append([])
            for column in range(COLS):
                if column % 2 == (row+1)%2:
                    if row<3:
                        self._board[row].append(Piece(row,column,RED))
                    elif row>4:
                        self._board[row].append(Piece(row,column,BLACK))
                    else:
                        self._board[row].append(0)
                else:
                    self._board[row].append(0)

        for row in range(ROWS):
            self._board.append([])
            for column in range(COLS):
                piece = self._board[row][column]
                if piece!=0:
                    piece.draw_circle(window)

    def draw_pieces_board(self, window):
        for row in range(ROWS):
            for column in range(COLS):
                piece = self._board[row][column]
                if piece!=0:
                    piece.draw_circle(window)

    def draw_suggested_pieces_board(self,color):
        pieces_in_position = self.get_pieces_attack_position(color)
        
        reccommended_pieces = []
        if  self._MUST_ATTACK and len(pieces_in_position)>0:
            for row in range(ROWS):
                for col in range(COLS):
                    if self._board[row][col]!=0 and (row,col) in pieces_in_position:
                        reccommended_pieces.append((row,col))
                        #self._board[row][col].draw_suggested(window) 

        else:
            for row in range(ROWS):
                for col in range(COLS):
                    if self._board[row][col]!=0 and self._board[row][col].color==color and len(self.selected_piece(col, row, color, pieces_in_position))>0:
                        reccommended_pieces.append((row,col))
                        #self._board[row][col].draw_suggested(window) 

        return reccommended_pieces
                    


    def get_num_pieces_attack_positions(self, color):
        return len(self.get_pieces_attack_position(color))
    
    def get_pieces_can_be_captured(self,color):
        sum=0

        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                if piece!=0 and piece.color == color:
                    if not self.out_of_bounds(row-1,col-1):
                        point1 = self.board[row-1][col-1]
                    else: point1 = None

                    if not self.out_of_bounds(row-1,col+1):
                        point2 = self.board[row-1][col+1]
                    else: point2 = None


                    if not self.out_of_bounds(row+1,col-1):
                        point3 = self.board[row+1][col-1]
                    else: point3 = None


                    if not self.out_of_bounds(row+1,col+1):
                        point4 = self.board[row+1][col+1]
                    else: point4 = None


                    if (point1 != None and point1!=0) and (point4 != None and point4==0) and (point1.direction==1 or point1.is_queen) and point1.color!=color:
                        sum+=1

                    if (point2 != None and point2!=0) and (point3 != None and point3==0) and (point2.direction==1 or point2.is_queen) and point2.color!=color:
                        sum+=1

                    if (point3 != None and point3!=0) and (point2 != None and point2==0) and (point3.direction==-1 or point3.is_queen) and point3.color!=color:
                        sum+=1

                    if (point4 != None and point4!=0) and (point1 != None and point1==0) and (point4.direction==-1 or point4.is_queen) and point4.color!=color:
                        sum+=1

        return sum

    def get_pieces_corner(self, color):
        sum=4

        if self._board[0][0]==0 or self._board[0][0].color!=color:
            sum-=1
        if self._board[0][7]==0 or self._board[0][7].color!=color:
            sum-=1
        if self._board[7][0]==0 or self._board[7][0].color!=color:
            sum-=1
        if self._board[7][7]==0 or self._board[7][7].color!=color:
            sum-=1

        return sum
    
    def get_pieces_wall(self, color):
        sum = 0

        for i in range(1,7):
            if self._board[0][i]!=0 and self._board[0][i].color==color:
                sum+=1
            if self._board[i][0]!=0 and self._board[i][0].color==color:
                sum+=1
            if self._board[7][i]!=0 and self._board[7][i].color==color:
                sum+=1
            if self._board[i][7]!=0 and self._board[i][7].color==color:
                sum+=1

        return sum 

    def get_advanced_pieces(self, color):
        sum = 0

        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                if piece!=0 and color == RED and row > ROWS//2-1:
                    sum+=1
                elif piece!=0 and color == BLACK and row < ROWS//2+1:
                    sum+=1
        
        return sum


    def check_draw_possible_move(self, row, column, player):
        if(not self.out_of_bounds(row,column) and self._board[row][column]==0):
            return row, column
        
        elif(not self.out_of_bounds(row, column) and self._board[row][column]!=0 and self._board[row][column].color!=player.color):
            ##### ovde greksa kad je kraljica ######
            if not player.is_queen:
                row_temp = row+player.direction
                if column-player.column>0:
                    column_temp=column+abs(player.direction)
                elif column-player.column<0:
                    column_temp=column-abs(player.direction)
            else:
                if row>player.row:
                    row_temp = row+1
                else:
                    row_temp = row-1

                if column-player.column>0:
                    column_temp=column+1
                elif column-player.column<0:
                    column_temp=column-1

            if(not self.out_of_bounds(row_temp,column_temp) and self._board[row_temp][column_temp]==0):
                return row_temp, column_temp
        
        return None, None     

    def get_pieces_attack_position(self, player_color):
        available_pieces = []

        for row in range(ROWS):
            for column in range(COLS):
                if self._board[row][column]==0 or (self._board[row][column]!=0 and self._board[row][column].color!=player_color): continue

                piece_analizing = self._board[row][column]
                
                row_temp = row + piece_analizing.direction
                column_temp1 = column-1
                column_temp2 = column+1

                if not self.out_of_bounds(row_temp, column_temp1) and (self._board[row_temp][column_temp1]!=0 and 
                                                self._board[row_temp][column_temp1].color != piece_analizing.color): 
                    
                    if not self.out_of_bounds(row_temp+piece_analizing.direction, column_temp1-1) and self._board[row_temp+piece_analizing.direction][column_temp1-1]==0:
                        available_pieces.append((row, column))
                
                if not self.out_of_bounds(row_temp, column_temp2) and (self._board[row_temp][column_temp2 ]!=0 
                                        and self._board[row_temp][column_temp2].color != piece_analizing.color):
                    
                    if not self.out_of_bounds(row_temp+piece_analizing.direction, column_temp2+1) and self._board[row_temp+piece_analizing.direction][column_temp2+1]==0:
                        available_pieces.append((row, column))

                if piece_analizing.is_queen:
                    row_queen = row + piece_analizing.direction*-1
                    if not self.out_of_bounds(row_queen, column_temp1) and (self._board[row_queen][column_temp1]!=0 and 
                                                self._board[row_queen][column_temp1].color != piece_analizing.color): 
                        
                        if not self.out_of_bounds(row_queen+piece_analizing.direction*-1, column_temp1-1) and self._board[row_temp+piece_analizing.direction*-1][column_temp1-1]==0:
                            available_pieces.append((row, column))

                
                    if not self.out_of_bounds(row_queen, column_temp2) and (self._board[row_queen][column_temp2 ]!=0 
                                            and self._board[row_queen][column_temp2 ].color != piece_analizing.color):
                        
                        if not self.out_of_bounds(row_queen+piece_analizing.direction*-1, column_temp2+1) and self._board[row_temp+piece_analizing.direction*-1][column_temp2+1]==0:
                            available_pieces.append((row, column))
                                          
        return available_pieces

        
    def check_draw_possible_mustattack(self, player, possible_moves):
        if self._MUST_ATTACK:
            save_moves = []

            for move in possible_moves:
                
                move_row = move[0]
                move_column = move[1]
                
                if move_row == None or move_column == None: continue

                if abs(move_row-player.row)>1 and abs(move_column-player.column)>1:
                    save_moves.append(move)

            if len(save_moves)>0: return save_moves        
        return possible_moves

        

    def selected_piece(self, position_col, position_row, player, pieces_attack_position):
        if self._MUST_ATTACK: 
            pieces_attack_position = self.get_pieces_attack_position(player)
            if len(pieces_attack_position)>0 and not (position_row, position_col) in pieces_attack_position: return []

        if(self._board[position_row][position_col]!=0 and self._board[position_row][position_col].color==player):
            possible_moves = []

            can_move_row = self._board[position_row][position_col].direction+position_row

            can_move_col1 = position_col+1
            can_move_col2 = position_col-1
            
            moves_check_mustattack = []

            can_move_row1, can_move_col1 = self.check_draw_possible_move(can_move_row, can_move_col1, self._board[position_row][position_col])
            moves_check_mustattack.append((can_move_row1, can_move_col1))

            can_move_row2, can_move_col2 = self.check_draw_possible_move(can_move_row, can_move_col2, self._board[position_row][position_col])
            moves_check_mustattack.append((can_move_row2, can_move_col2))


            if self._board[position_row][position_col].is_queen:
                can_move_row_queen = self._board[position_row][position_col].direction*(-1)+position_row
                can_move_col1_queen = position_col+1
                can_move_col2_queen = position_col-1

                can_move_row3, can_move_col3 = self.check_draw_possible_move(can_move_row_queen, can_move_col1_queen, self._board[position_row][position_col])
                moves_check_mustattack.append((can_move_row3, can_move_col3 ))

                can_move_row4, can_move_col4 = self.check_draw_possible_move(can_move_row_queen, can_move_col2_queen, self._board[position_row][position_col])
                moves_check_mustattack.append((can_move_row4, can_move_col4))
            
            moves_check_mustattack = self.check_draw_possible_mustattack(self._board[position_row][position_col], moves_check_mustattack)

            if (can_move_row1!=None and can_move_col1!=None and (can_move_row1, can_move_col1) in moves_check_mustattack):
                possible_moves.append((can_move_row1, can_move_col1))
            
            if (can_move_row2!=None and can_move_col2!=None and (can_move_row2, can_move_col2) in moves_check_mustattack):
                possible_moves.append((can_move_row2, can_move_col2))

            if (self._board[position_row][position_col].is_queen and can_move_row3!=None and can_move_col3!=None and (can_move_row3, can_move_col3) in moves_check_mustattack):
                possible_moves.append((can_move_row3, can_move_col3))

            if (self._board[position_row][position_col].is_queen and can_move_row4!=None and can_move_col4!=None and (can_move_row4, can_move_col4) in moves_check_mustattack):
                possible_moves.append((can_move_row4, can_move_col4))

            return possible_moves
        else:
            return False

    def remove_piece(self, player, move_col, move_row):
        if move_row>player.row:
            remove_piece_row = move_row-1
            if move_col>player.column:
                remove_piece_col = move_col-1
            else:
                remove_piece_col = move_col+1
        else:
            remove_piece_row = player.row-1
            if move_col>player.column:
                remove_piece_col = move_col-1
            else:
                remove_piece_col = move_col+1

        piece_color = self._board[remove_piece_row][remove_piece_col].color
        piece_is_queen = self._board[remove_piece_row][remove_piece_col].is_queen
        self._board[remove_piece_row][remove_piece_col] = 0

        if piece_color == BLACK: self._black_pieces_left-=1
        else: self._red_pieces_left-=1

        if piece_is_queen:
            if piece_color == BLACK: self._black_piece_queens-=1
            else: self._red_piece_queens-=1       

    def move_piece(self, possible_moves, piece_col, piece_row, move_col, move_row):
        for move in possible_moves:
            possible_move_row = move[0]
            possible_move_col = move[1]
            
            if((not self.out_of_bounds(possible_move_row, possible_move_col)) and self._board[possible_move_row][possible_move_col]==0 
               and (possible_move_row==move_row and possible_move_col==move_col)):
                
                if abs(move_row-piece_row)==2:
                    self.remove_piece(self._board[piece_row][piece_col], move_col, move_row)
                
                self._board[move_row][move_col] = self._board[piece_row][piece_col]
                self._board[move_row][move_col].column = move_col
                self._board[move_row][move_col].row = move_row

                self._board[piece_row][piece_col] = 0

                if(self._board[move_row][move_col].color == BLACK and move_row==0):
                    self._board[move_row][move_col].is_queen = True
                elif(self._board[move_row][move_col].color == RED and move_row==ROWS-1):
                    self._board[move_row][move_col].is_queen = True

                return True
            
            elif((self.out_of_bounds(possible_move_row, possible_move_col) or self._board[possible_move_row][possible_move_col]!=0 )
               and (possible_move_row==move_row and possible_move_col==move_col)):
                return False
            
    def get_pieces_movement_algo(self, color):
        hash_map = HashMap()

        pieces_in_position = self.get_pieces_attack_position(color)
        moves=[]
        if  self._MUST_ATTACK and len(pieces_in_position)>0:
            for row in range(ROWS):
                for col in range(COLS):
                    if self._board[row][col]==0 or not (row,col) in pieces_in_position: continue

                    possible_moves = self.selected_piece(col, row, color, pieces_in_position)
                    for possible_move in possible_moves:
                       moves.append([(row,col), possible_move])
                        

        else:
            for row in range(ROWS):
                for col in range(COLS):
                    if self._board[row][col]==0 or self._board[row][col].color!=color :continue

                    possible_moves= self.selected_piece(col, row, color, pieces_in_position)
                    for possible_move in possible_moves:
                       moves.append([(row,col), possible_move])


        return moves

        #return hash_map => [suggested_piece, [moveable_points]]
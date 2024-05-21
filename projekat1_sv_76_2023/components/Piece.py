from .constants import *
import pygame

class Piece:
    def __init__(self, row, column, color):
        self.x=0
        self.y=0
        self.row = row
        self.column = column
        self.color = color
        self.is_queen = False

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

        self.position()
        
    
    def position(self):
        self.x = SQUARE_SIZE*self.column+SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row+SQUARE_SIZE//2
        
    def become_queen(self):
        self.is_queend=True

    def draw_circle(self,window):
        self.position()
        pygame.draw.circle(window, self.color, (self.x,self.y), SQUARE_SIZE//2-10)

    def draw_suggested(self, window):
        self.position()
        pygame.draw.rect(window, WHITE, (self.column*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    
    def is_next_to_wall(self):
        return self.row == 0 or self.row == 7 or self.col == 0 or self.col == 7
    
    def __str__(self):
        if self.color == BLACK:
            col = 'black'
        else:
            col = 'red'

        if self.is_queen:
            return col+' queen'
        else:
            return col+' normal'
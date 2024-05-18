import pygame
from components.constants import *
from components.Board import Board
import sys


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
board = Board()

def start_menu():
    pass

def main():
    play = True
    player_turn = BLACK
    board.draw_positions(WINDOW)
    board.draw_pieces_board_beggining(WINDOW)
    pygame.display.update()

    while play:
        pygame.time.Clock().tick(60)

        player_made_move = False
        while not player_made_move:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    piece_pos_col, piece_pos_row = pygame.mouse.get_pos()[0]//SQUARE_SIZE, pygame.mouse.get_pos()[1]//SQUARE_SIZE

                    possible_moves = board.selected_piece(WINDOW, piece_pos_col, piece_pos_row, player_turn)
                    if(possible_moves == False): continue
                    
                    waiting = True

                    while waiting:
                        for event_waiting in pygame.event.get():

                            if event_waiting.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event_waiting.type == pygame.MOUSEBUTTONDOWN:
                                move_pos_col, move_pos_row = pygame.mouse.get_pos()[0]//SQUARE_SIZE, pygame.mouse.get_pos()[1]//SQUARE_SIZE
                                
                                moved = board.move_piece(WINDOW, possible_moves, piece_pos_col, piece_pos_row, move_pos_col, move_pos_row)

                                if moved: 
                                    player_made_move = True

                                waiting = False        
                                        

                if event.type==pygame.QUIT:
                    player_made_move = True
                    play=False

            board.draw_positions(WINDOW)
            board.draw_pieces_board(WINDOW)
            pygame.display.update()

        if board.black_pieces_left==0 or board.red_pieces_left==0:
            pygame.quit()
            sys.exit()


        if player_turn==BLACK: player_turn=RED
        else: player_turn=BLACK

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()

    main()
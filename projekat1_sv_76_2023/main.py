import pygame
from components.constants import *
from components.Board import Board
import sys
from components.algorithm import minimax


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
board = Board()

def start_menu():
    pass

def update_display(color):
    board.draw_positions(WINDOW)
    board.draw_suggested_pieces_board(WINDOW, color)
    board.draw_pieces_board(WINDOW)
    pygame.display.update()

def main():
    play = True
    player_turn = BLACK
    
    board.draw_positions(WINDOW)
    board.draw_pieces_board_beggining(WINDOW)
    pygame.display.update()

    while play:
        pygame.time.Clock().tick(60)

        update_display(player_turn)

        #minimax(board, None, None, None, None, None)

        player_made_move = False
        while not player_made_move: # and player_turn==BLACK
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    piece_pos_col, piece_pos_row = pygame.mouse.get_pos()[0]//SQUARE_SIZE, pygame.mouse.get_pos()[1]//SQUARE_SIZE

                    possible_moves = board.selected_piece(piece_pos_col, piece_pos_row, player_turn)
                    if(possible_moves == False): continue

                    for move in possible_moves:
                        pygame.draw.rect(WINDOW, GREEN, (move[1] * SQUARE_SIZE, move[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.display.update()
                    
                    waiting = True

                    while waiting:
                        for event_waiting in pygame.event.get():

                            if event_waiting.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event_waiting.type == pygame.MOUSEBUTTONDOWN:
                                move_pos_col, move_pos_row = pygame.mouse.get_pos()[0]//SQUARE_SIZE, pygame.mouse.get_pos()[1]//SQUARE_SIZE
                                
                                moved = board.move_piece(possible_moves, piece_pos_col, piece_pos_row, move_pos_col, move_pos_row)

                                if moved: 
                                    player_made_move = True

                                waiting = False                                        

                if event.type==pygame.QUIT:
                    player_made_move = True
                    play=False

            update_display(player_turn)

        if player_turn == RED:
            print('red')

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
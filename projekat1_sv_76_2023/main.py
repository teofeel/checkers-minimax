import pygame
from components.constants import *
import components.constants as constants
from components.Board import Board
import sys
from components.algorithm import *
import time

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
board = Board()
times = []
def start_menu():
    WINDOW.fill(WHITE)

    rect_width = 200
    rect_height = 100

    x = (HEIGHT - rect_width) // 2
    y1= (HEIGHT - 2 * rect_height - 10) // 2  
    y2 = y1 + rect_height + 10

    font = pygame.font.SysFont(None, 36)

    must_att = font.render('Must attack', True, WHITE)
    must_not_att = font.render('Free movement', True, WHITE)

    must_att_rect = must_att.get_rect(center=(x + rect_width // 2, y1 + rect_height // 2))
    must_not_att_rect = must_not_att.get_rect(center=(x + rect_width // 2, y2 + rect_height // 2))

    wait = True
    while wait:
        pygame.draw.rect(WINDOW, BLACK, (x, y1, rect_width, rect_height))  
        pygame.draw.rect(WINDOW, BLACK, (x, y2, rect_width, rect_height))  

        WINDOW.blit(must_att, must_att_rect)
        WINDOW.blit(must_not_att, must_not_att_rect)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if x <= mouse_pos[0] <= x + rect_width:
                    if y1 <= mouse_pos[1] <= y1 + rect_height:   
                       
                        return True
                    
                    elif y2 <= mouse_pos[1] <= y2 + rect_height:
                       
                        return False


def update_display(color):
    board.draw_positions(WINDOW)
    reccommended = board.draw_suggested_pieces_board(color)

    for item in reccommended:
        board.board[item[0]][item[1]].draw_suggested(WINDOW)

    board.draw_pieces_board(WINDOW)
    pygame.display.update()

def show_next_player():
    pass

def show_draw():
    pass

def main():
    play = True
    player_turn = BLACK

    board.draw_positions(WINDOW)
    board.draw_pieces_board_beggining(WINDOW)
    pygame.display.update()

    while play:
        pygame.time.Clock().tick(60)

        update_display(player_turn)

        if player_turn == RED:
            before = time.time()
           
            
            move = make_move(board, RED, 4)
            #time.sleep(650000)

            board.move_piece([move[1]], move[0][1], move[0][0], move[1][1], move[1][0])

            times.append(time.time()-before)
            print(time.time()-before)

            
            

        player_made_move = False
        while not player_made_move and player_turn==BLACK: 
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    piece_pos_col, piece_pos_row = pygame.mouse.get_pos()[0]//SQUARE_SIZE, pygame.mouse.get_pos()[1]//SQUARE_SIZE

                    possible_moves = board.selected_piece(piece_pos_col, piece_pos_row, player_turn, board.get_pieces_attack_position(BLACK))
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

        

        if board.black_pieces_left==0 or board.red_pieces_left==0:
           print(sum(times)/len(times))
           pygame.quit()
           sys.exit()

        if player_turn==BLACK: player_turn=RED
        else: player_turn=BLACK

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    
    board.MUST_ATTACK = start_menu()

    main()
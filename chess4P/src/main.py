'''
Name: Al-Baraa El-Hag
Date: Sept 29 2019
'''

## Part 0: Importing
import numpy as np
import pygame as pygame
import moves

## Running Game
def run_game(chess_board):
    screen = pygame.display.set_mode((chess_board.width, chess_board.height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color(chess_board.bg))

    running = True
    new_turn = True
    sq_selected = () # no square is selected, keep track of last click
    player_clicks = [] # keep track of the player clicks (two tuples [(6, 4), (4, 4)])

    while running:
            if new_turn:
                chess_board.get_moves()
                new_turn = False

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    # pygame.display.quit()
                    running = False
                
                # Mouse events
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos() # (x, y) location of mouse
                    col = location[0]//chess_board.sq_size
                    row = location[1]//chess_board.sq_size

                    # the user clicked the same square twice (undo)
                    if (sq_selected == (row, col) or
                        chess_board.board[row, col] == 'xx' or
                        (chess_board.board[row, col] == '--' and len(player_clicks) == 0)): 
                        sq_selected = () # deselect
                        player_clicks = []

                    # append for first and second clicks
                    else:
                        sq_selected = (row, col)
                        player_clicks.append(sq_selected) 

                    # after the users second click
                    if len(player_clicks) == 2: 
                        # Equals true, if new move is played
                        new_turn = chess_board.move_piece(player_clicks) 
                        sq_selected = ()
                        player_clicks = []

                # Keyboard events
                elif e.type == pygame.KEYDOWN:

                    # Undo when z is pressed
                    if e.key == pygame.K_z:
                        chess_board.move_undo()


            chess_board.draw_all(screen, sq_selected,
                                chess_board.turn_sequence[0],
                                chess_board.moves_ava)
            clock.tick(chess_board.max_fps)
            pygame.display.flip()


if __name__ == "__main__":
    chess_board = moves.Moves()
    run_game(chess_board)
    pygame.display.quit()


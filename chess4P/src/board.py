import numpy as np
import pygame
import main
import moves

class ChessBoard():

    '''
    This class is responsible for storing all the information about the current state
    of a chess game. 
    '''

    def __init__(self):
        self.board = np.array([
            ['xx', 'xx', 'xx', 'yR', 'yN', 'yB', 'yQ', 'yK', 'yB', 'yN', 'yR', 'xx', 'xx', 'xx'],
            ['xx', 'xx', 'xx', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', 'yP', 'xx', 'xx', 'xx'],
            ['xx', 'xx', 'xx', '--', '--', '--', '--', '--', '--', '--', '--', 'xx', 'xx', 'xx'],

            ['bR', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gR'],
            ['bN', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gN'],
            ['bB', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gB'],
            ['bK', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gQ'],
            ['bQ', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gK'],
            ['bB', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gB'],
            ['bN', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gN'],
            ['bR', 'bP', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', 'gP', 'gR'],

            ['xx', 'xx', 'xx', '--', '--', '--', '--', '--', '--', '--', '--', 'xx', 'xx', 'xx'],
            ['xx', 'xx', 'xx', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', 'rP', 'xx', 'xx', 'xx'],
            ['xx', 'xx', 'xx', 'rR', 'rN', 'rB', 'rQ', 'rK', 'rB', 'rN', 'rR', 'xx', 'xx', 'xx']])
        
        self.dimension = 14
        self.sq_size = 50
        self.width = self.height = self.sq_size * self.dimension
        self.max_fps = 15
        self.bg = "#3C3A36"

        self.highlight_color = {
            "r": 'Red',
            "b": 'Blue',
            "y": 'Yellow',
            "g": 'Green'
        }
        self.load_images()


    def load_images(self):
        '''
        Initialize a global dictionary of images. This will be called once in the main
        '''
        self.images = {}

        colors = ['r', 'b', 'y', 'g']
        pieces = ['P', 'R', 'N', 'B', 'Q', 'K']

        for color in colors:
            for piece in pieces:
                folder_loc = "../resources/png/"
                piece_label = color+piece
                piece_loc = folder_loc + piece_label + ".png"

                self.images[piece_label] = pygame.transform.scale(
                    pygame.image.load(piece_loc), (self.sq_size, self.sq_size))


    def draw_board(self, screen):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(self.dimension):
            for col in range(self.dimension):
                # Draw real squares
                if self.board[row, col] != 'xx':
                    color = colors[((row + col) % 2)]
                    pygame.draw.rect(screen, color, 
                                pygame.Rect((col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size)))

                # Draw squares that are not playable
                else:
                    pygame.draw.rect(screen, pygame.Color(self.bg),
                        pygame.Rect((col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size)))


    def draw_highlights(self, screen, sq_selected, turn, moves_ava):

        if sq_selected != ():
            row, col = sq_selected
            if self.board[row, col][0] == turn:
                # Highlight selected square
                s = pygame.Surface((self.sq_size, self.sq_size))
                s.set_alpha(90) # 0 transparent; 255 opaque
                s.fill(pygame.Color(self.highlight_color[turn]))
                screen.blit(s, (col*self.sq_size, row*self.sq_size))

                s.set_alpha(40) # 0 transparent; 255 opaque
                s.fill(pygame.Color(self.highlight_color[turn]))
                for move in moves_ava:
                    if move[0] == list(sq_selected):
                        screen.blit(s, (move[1][1]*self.sq_size,
                                        move[1][0]*self.sq_size))


    def draw_pieces(self, screen):
        for row in range(self.dimension):
            for col in range(self.dimension):
                piece = self.board[row, col]

                if piece != '--' and piece != 'xx':
                    screen.blit(self.images[piece],
                                pygame.Rect(col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size))

    def draw_all(self, screen, sq_selected, turn, moves_ava):
        self.draw_board(screen)
        self.draw_highlights(screen, sq_selected, turn, moves_ava)
        self.draw_pieces(screen)


if __name__ == "__main__":
    chess_board = moves.Moves()
    main.run_game(chess_board)
    pygame.display.quit()



## Part 0: Importing
import numpy as np
import pygame as p

class chessBoard():

    '''
    This class is responsible for storing all the information about the current state of a chess game. 
    It will also be responsible for determining the valid moves at the current state. 
    It will also keep a move log
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

        self.redToMove = True
        self.moveLog = []

        self.dimension = 14
        self.sq_size = 50
        self.width = self.height = self.sq_size * self.dimension
        self.max_fs = 15
        self.bg = "#3C3A36"

        p.init()


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

                self.images[piece_label] = p.transform.scale(
                    p.image.load(piece_loc), (self.sq_size, self.sq_size))


    def draw_board(self):
        colors = [p.Color("white"), p.Color("gray")]
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.board[row, col] != 'xx':
                    color = colors[((row + col) % 2)]
                    p.draw.rect(self.screen, color, 
                                p.Rect((col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size)))
                else:
                    p.draw.rect(self.screen, p.Color(self.bg),
                        p.Rect((col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size)))


    def draw_pieces(self):
        for row in range(self.dimension):
            for col in range(self.dimension):
                piece = self.board[row, col]

                if piece != '--' and piece != 'xx':
                    self.screen.blit(self.images[piece],
                                p.Rect(col*self.sq_size, row*self.sq_size, self.sq_size, self.sq_size))

    def pygame_stuff(self):
        self.screen = p.display.set_mode((self.width, self.height))
        clock = p.time.Clock()
        self.screen.fill(p.Color(self.bg))
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False

            self.draw_board()
            self.draw_pieces()
        clock.tick(self.max_fps)
        p.display.flip()



if __name__ == "__main__":
    A = chessBoard()
    A.load_images()
    A.pygame_stuff()
    p.display.quit()

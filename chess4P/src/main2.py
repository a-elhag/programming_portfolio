"""
Author: Al-Baraa El-Hag
Date: Sept 30, 2020

Description: This class is responsible for storing all the information
             about the current state of a chess game. 
             It will also be responsible for determining the valid moves
             at the current state. It will also keep a move log
"""
## Part 0a: Importing
import numpy as np
import pygame as p

## Part 0b: Initializing Board
board = np.array([
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
    ['xx', 'xx', 'xx', 'rR', 'rN', 'rB', 'rQ', 'rK', 'rB', 'rN', 'rR', 'xx', 'xx', 'xx']
])

redToMove = True
moveLog = []

## Part 1: Pygame
p.init()
dimension = 14 # dimensions = 14x14
sq_size = 50
width = height = sq_size*dimension
max_fps = 15


def load_images():
    '''
    Initialize a global dictionary of images. This will be called once in the main
    '''
    images = {}

    colors = ['r', 'b', 'y', 'g']
    pieces = ['P', 'R', 'N', 'B', 'Q', 'K']

    for color in colors:
        for piece in pieces:
            folder_loc = "../resources/png/"
            piece_label = color+piece
            piece_loc = folder_loc + piece_label + ".png"

            images[piece_label] = p.transform.scale(
                p.image.load(piece_loc), (sq_size, sq_size))

    return images


## Part 2: Main Driver
bg = "#3C3A36"
def main():
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color(bg))
    images = load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                # p.display.quit()
                running = False

        draw_game_state(screen, board, images)
        clock.tick(max_fps)
        p.display.flip()

def draw_game_state(screen, board, images):
    '''
    Responsible for all the graphics on the current gamestate
    '''
    draw_board(screen) # draw squares on board
    draw_pieces(screen, board, images) # draw pieces on top of those squares

def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(dimension):
        for col in range(dimension):
            if board[row, col] != 'xx':
                color = colors[((row + col) % 2)]
                p.draw.rect(screen, color, 
                            p.Rect((col*sq_size, row*sq_size, sq_size, sq_size)))
            else:
                p.draw.rect(screen, p.Color(bg),
                    p.Rect((col*sq_size, row*sq_size, sq_size, sq_size)))


def draw_pieces(screen, board, images):
    for row in range(dimension):
        for col in range(dimension):
            piece = board[row, col]

            if piece != '--' and piece != 'xx':
                screen.blit(images[piece],
                            p.Rect(col*sq_size, row*sq_size, sq_size, sq_size))



if __name__ == "__main__":
    main()
    p.display.quit()
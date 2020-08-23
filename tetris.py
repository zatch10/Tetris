import pygame
import shape_arrays
from random import randint as rand

# Constants
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_d
)
WIDTH = 350
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128)]
BlockSize = 35
shapes = shape_arrays.get_shapes()


def create_grid():
    for x in range(WIDTH // BlockSize):
        for y in range(HEIGHT // BlockSize):
            rect = pygame.Rect(x * BlockSize, y * BlockSize, BlockSize, BlockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)


def check_wall():
    pass


def rotate_clockwise():
    pass


def rotate_anticlockwise():
    pass


def move_right():
    pass


def move_left():
    pass


def next_shape():
    shape_type = rand(0, len(shapes) - 1)
    shape_orient = rand(0, len(shapes[shape_type]) - 1)
    color_type = rand(0, len(colors) - 1)
    rows = len(shapes[shape_type][shape_orient])
    cols = len(shapes[shape_type][shape_orient][0])
    cur_shape = Piece(colors[color_type], shapes[shape_type], shape_orient, rows, cols)
    cur_shape.cur_orient = shapes[shape_type][shape_orient]
    print(shapes[shape_type][shape_orient])
    print(rows)
    print(cols)
    return cur_shape

def check_state():
    pass


def clear():
    pass


def move_down(cur_shape):
    if cur_shape.appeared is False:
        for y in range(cur_shape.cols):
            print(cur_shape.shape)
            if cur_shape.cur_orient[len(cur_shape.cur_orient) - 1][y] is 1:
                grid[cur_shape.cur_row][cur_shape.cur_col + y] = 1
        update_screen(cur_shape)
        cur_shape.appeared = True


def update_screen(cur_shape):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] is 0:
                rect = pygame.Rect(x * BlockSize, y * BlockSize, BlockSize, BlockSize)
                pygame.draw.rect(screen, WHITE, rect, 1)
            else:
                rect = pygame.Rect(x * BlockSize, y * BlockSize, BlockSize, BlockSize)
                pygame.draw.rect(screen, cur_shape.color, rect, 1)


def main():
    global RUNNING, screen, grid, CLOCK, FALLING
    pygame.init()
    RUNNING = True
    cur_shape = Piece()
    cur_shape.exists = False
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    grid = 20 * [10 * [0]]
    create_grid()
    while RUNNING:
        if cur_shape.exists is False:
            cur_shape = next_shape()
        move_down(cur_shape)
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    RUNNING = False

                if event.key == K_RIGHT:
                    move_right()

                if event.key == K_LEFT:
                    move_left()

                if event.key == K_a:
                    rotate_anticlockwise()

                if event.key == K_d:
                    rotate_clockwise()

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                RUNNING = False
        pygame.display.update()


class Piece:
    def __init__(self, color=None, shape=None, orient=None, rows=None, cols=None):
        self.color = color
        self.shape = shape
        self.orient = orient
        self.rows = rows
        self.cols = cols
        self.showing = 0
        self.appeared = False
        self.complete = False
        self.cur_row = 0
        self.cur_col = 3
        self.falling = True
        self.exists = True
        self.cur_orient = None



if __name__ == "__main__":
    main()

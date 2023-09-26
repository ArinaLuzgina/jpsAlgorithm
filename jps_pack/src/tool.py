from math import *
from PIL import Image
import numpy as np

def squareScreen(pg, sc,tile, matrix):
    xlenght = matrix.shape[1]
    ylenght = matrix.shape[0]
    [pg.draw.line(sc, (200, 200, 200), (tile * x, 0), (tile * x, ylenght * tile), 1) for x in range(xlenght)]
    [pg.draw.line(sc, (200, 200, 200), (0, tile * y), (xlenght * tile, tile * y)) for y in range(ylenght)]
    pass

def drawBorders(pg, sc, tile, matrix):
    xlenght = matrix.shape[1]
    ylenght = matrix.shape[0]
    [[pg.draw.rect(sc, (0, 0, 0), (x * tile, y * tile, tile, tile)) for x in range(xlenght) if matrix[y][x]] for y in range(ylenght)]
    pass

def get_rect(x, y, tile):
    return x*tile, y * tile, tile * 2, tile * 2


def get_circle(x, y, tile):
    return (x * tile + tile // 2, y * tile + tile // 2), 2


def get_line(start, end, tile):
    return (start[0] * tile + tile // 2, start[1] * tile + tile // 2), (end[0] * tile + tile // 2, end[1] * tile + tile // 2)


def makeCounter(count, color, pg, sc):
    font = pg.font.Font(None, 100)
    text = font.render(str(count), True, color)
    text_x = text.get_width() // 2
    text_y = text.get_height() // 2

    sc.blit(text, (text_x, text_y))
    return sc



def get_next_node(x, y, cols, rows, graph):
    def check_next_node(
        x, y): return True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
    matrix = []
    for dx, dy in ways:
        if check_next_node(x + dx, y + dy) and graph[y + dy][x + dx] == 0:
            if abs(dx) + abs(dy) < 2:
                matrix.append((1, (x + dx, y + dy)))
            elif abs(dx) + abs(dy) >= 2:
                matrix.append((sqrt(2), (x + dx, y + dy)))
    return matrix


def pathLenghtCount(x, y, px, py):
    dx = abs(x - px)
    dy = abs(y - py)
    if dy == 0:
        return dx
    elif dx == 0:
        return dy
    elif dx > dy:
        return sqrt(2) * dy + dx - dy
    else:
        return sqrt(2) * dx + dy - dx


def get_click_mouse(pg, sc, tile):
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x//tile, y // tile
    click = pg.mouse.get_pressed()

    return (grid_x, grid_y) if click[0] else False


def makeMaze(imgName):
    img = Image.open(imgName)
    gray = img.convert('L')
    bw = gray.point(lambda x: 1 if x<128 else 0)
    ar = np.asarray(bw)
    return ar

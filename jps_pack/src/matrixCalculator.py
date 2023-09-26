import numpy as np
import pygame as pg

matrix1 = np.zeros((5, 10))
matrix1 = np.random.choice([0, 1], size=(5, 10))
print(matrix1)
tile = 50
xlenght = matrix1.shape[0]
ylenght = matrix1.shape[1]
FPS = 30 # частота кадров в секунду
# создаем игру и окно
pg.init()
sc = pg.display.set_mode((tile * ylenght, tile * xlenght))
pg.display.set_caption("My Game")
clock = pg.time.Clock()
# Цикл игры
running = True

def squareScreen(pg, sc,tile, matrix):
    xlenght = matrix.shape[1]
    ylenght = matrix.shape[0]
    [pg.draw.line(sc, (0, 0, 0), (tile * x, 0), (tile * x, ylenght * tile)) for x in range(xlenght)]
    [pg.draw.line(sc, (0, 0, 0), (0, tile * y), (xlenght * tile, tile * y)) for y in range(ylenght)]
    pass
def getRect(pg, sc, tile, matrix):
    xlenght = matrix.shape[1]
    ylenght = matrix.shape[0]
    [[pg.draw.rect(sc, (0, 0, 0), (x * tile, y * tile, tile, tile)) for x in range(xlenght) if matrix[y][x]] for y in range(ylenght)]
    pg.display.flip()
    pass

while running:
    sc.fill((255, 255, 255))
    # [[pg.draw.rect(sc, pg.Color("black"), get_rect(x, y, tile))
    #       for x, col in enumerate(row) if int(col)] for y, row in enumerate(matrix1)]
    squareScreen(pg, sc,tile,  matrix1)
    getRect(pg, sc, tile, matrix1)
    for event in pg.event.get():
    # проверить закрытие окна
        if event.type == pg.QUIT:
            running = False
    clock.tick(FPS)
    pg.display.flip()
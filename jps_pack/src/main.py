import pygame as pg
from jpsAlgorithm import jps
from math import *
import numpy as np
from tool import get_click_mouse, get_circle, makeMaze, squareScreen, drawBorders
from drawing import jpsDrawing
import time


def prepScreen(pg, sc, tile, graph, flag, new, pathJ, start, goal):
    sc.fill(pg.Color('white'))
    squareScreen(pg, sc, tile, graph)
    drawBorders(pg, sc, tile, graph)
    mousePose = pg.mouse.get_pos()
    x, y = int(mousePose[1])//tile, int(mousePose[0]) // tile
    pg.draw.circle(sc, pg.Color('red'), *get_circle(y, x, tile))
    if start and not goal:
        pg.draw.circle(sc, pg.Color("navy"), *
                       get_circle(start[1], start[0], tile))
    if goal:
        pg.draw.circle(sc, pg.Color("navy"), *
                       get_circle(start[1], start[0], tile))
        pg.draw.circle(sc, pg.Color("navy"), *
                       get_circle(goal[1], goal[0], tile))
    if flag == 1 and not new:
        pg, sc = jpsDrawing(pathJ, start, tile, pg, sc)


def main(pg):
    tile = 3
    rows = 13
    cols = 23
    goal = 0
    start = 0
    counter = 0
    flag = 0
    new = False
    robotPose = [0, 0]
    robotCondition = 0
    pathJ = []
    actPath = False

    graph = makeMaze(
        'C:/Users/Арина Лузгина/Desktop/Scripts/Python/navigation/jps_pack/images/maze2_0.png')
    cols, rows = graph.shape

    pg.init()
    sc = pg.display.set_mode([int(cols * tile), int(rows * tile)])
    clock = pg.time.Clock()

    while True:
        mouse_pos = get_click_mouse(pg, sc, tile)
        prepScreen(pg, sc, tile, graph, flag, new, pathJ, start, goal)
        pg.display.flip()

        if mouse_pos:
            if counter == 0:
                start = (int(mouse_pos[1]), int(mouse_pos[0]))
                counter += 1
                goal = None
                flag = 0
                print(start)
            else:
                counter = 0
                goal = (int(mouse_pos[1]), int(mouse_pos[0]))
                print(goal)
        if goal:

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        flag = 1
                    elif event.key == pg.K_2:
                        flag = 2

                    new = True
            if new:
                if flag == 1:
                    startT = time.time()
                    pathJ = jps(start, goal, graph)
                    endT = time.time()
                    print(endT - startT)

                new = False
                actPath = True
        if flag == 1 and not new and actPath:
            robotCondition = 0
            robotPose = [pathJ[0][1], pathJ[0][0]]
            prepScreen(pg, sc, tile, graph, flag, new, pathJ, start, goal)
            pg.draw.circle(sc, (255, 0, 255), *get_circle(*robotPose, tile))
            pg.display.flip()
            while robotPose != [goal[1], goal[0]]:
                deltaT = 0.1
                tS = time.time()
                while time.time() - deltaT < tS:
                    clock.tick(10)
                if pathJ[robotCondition][0] == pathJ[robotCondition + 1][0]:
                    dY = 0
                elif (pathJ[robotCondition][0] - pathJ[robotCondition + 1][0]) > 0:
                    if (robotPose[1] - pathJ[robotCondition+1][0]) > ((pathJ[robotCondition][0] - pathJ[robotCondition + 1][0]) // 100):
                        dY = (pathJ[robotCondition+1][0] - robotPose[1])

                    else:
                        dY = (pathJ[robotCondition][0] -
                              pathJ[robotCondition + 1][0]) // 100 * -1

                else:
                    if (pathJ[robotCondition+1][0] - robotPose[1]) > ((pathJ[robotCondition + 1][0] - pathJ[robotCondition][0]) // 100):
                        dY = (pathJ[robotCondition+1][0] - robotPose[1])

                    else:
                        dY = (pathJ[robotCondition][0] -
                              pathJ[robotCondition + 1][0]) // 100 * -1

                if pathJ[robotCondition][1] == pathJ[robotCondition + 1][1]:
                    dX = 0
                elif (pathJ[robotCondition][1] - pathJ[robotCondition + 1][1]) > 0:
                    if (robotPose[0] - pathJ[robotCondition+1][1]) > ((pathJ[robotCondition][1] - pathJ[robotCondition + 1][1]) // 100):
                        dX = (pathJ[robotCondition+1][1] - robotPose[0])

                    else:
                        dX = ((pathJ[robotCondition][1] -
                              pathJ[robotCondition + 1][1]) // 100) * -1

                else:
                    if (pathJ[robotCondition+1][1] - robotPose[0]) > ((pathJ[robotCondition + 1][1] - pathJ[robotCondition][1]) // 100):
                        dX = (pathJ[robotCondition+1][1] - robotPose[0])

                    else:
                        dX = ((pathJ[robotCondition][1] -
                              pathJ[robotCondition + 1][1]) // 100) * -1
                
                robotPose[0] += dX
                robotPose[1] += dY

                if (robotPose[1], robotPose[0]) == pathJ[robotCondition + 1]:
                    robotCondition += 1
                prepScreen(pg, sc, tile, graph, flag, new, pathJ, start, goal)
                pg.draw.circle(sc, (255, 0, 255), *
                               get_circle(*robotPose, tile))
                pg.display.flip()
                clock.tick(10)
                actPath = False
                pass
        [exit() for event in pg.event.get() if event.type == pg.QUIT]

        clock.tick(7)


if __name__ == "__main__":
    main(pg)

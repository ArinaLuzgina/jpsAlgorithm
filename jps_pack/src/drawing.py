from tool import get_line, get_circle, makeCounter, pathLenghtCount


def jpsDrawing(path, start, tile, pg, sc):
    pathLenght = 0
    prev = (start[1], start[0])
    for i in path:
        x = i[1]
        y = i[0]
        pathLenght += pathLenghtCount(x, y, prev[0], prev[1])
        pg.draw.circle(sc, pg.Color('green'), *get_circle(x, y, tile))
        line = get_line(prev, (x, y), tile)
        pg.draw.line(sc, pg.Color('green'), line[0], line[1], width=1)
        prev = (i[1], i[0])
    sc = makeCounter(pathLenght, (255, 0, 0), pg, sc)
    return (pg, sc)

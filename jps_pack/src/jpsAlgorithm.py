from heapq import *
import math as m

def heurustic_func(ch1, ch2):
    x = abs(ch1[0] - ch2[0])
    y = abs(ch1[0] - ch2[0])
    if x > y:
        return m.sqrt(2) * y + (x - y)
    else:
        return m.sqrt(2) * x + (y - x)

def blocked(cX, cY, dX, dY, matrix):
    
    if cX + dX < 0 or cX + dX >= matrix.shape[1]:
        return True
    if cY + dY < 0 or cY + dY >= matrix.shape[0]:
        return True
    if dX != 0 and dY != 0:
        if matrix[(cX + dX) ][cY ] == 1 and matrix[cX ][(cY + dY) ] == 1:
            return True
        if matrix[(cX + dX) ][(cY + dY) ] == 1:
            return True
    else:
        if dX != 0:
            if matrix[(cX + dX) ][cY ] == 1:
                return True
        else:
            if matrix[cX ][(cY + dY) ] == 1:
                return True
    return False

def direction(x, y, endX, endY):
    dir1 = int(m.copysign(1, x - endX))
    dir2 = int(m.copysign(1, y - endY))
    if x - endX == 0:
        dir1 = 0
    if y - endY == 0:
        dir2 = 0
    return(dir1, dir2)

def dblock(cX, cY, dX, dY, matrix):
    if matrix[cX - dX][cY ] == 1 and matrix[cX ][cY - dY ] == 1:
        return True
    else:
        return False

def nodeNeighbours(cX, cY, parent, matrix):
    neighbours = []
    if type(parent) != tuple:
        for i, j in [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]:
            if not blocked(cX, cY, i, j, matrix):
                neighbours.append((cX + i, cY + j))

        return neighbours
    dX, dY = direction(cX, cY, parent[0], parent[1])

    if dX != 0 and dY != 0:
        if not blocked(cX, cY, 0, dY, matrix):
            neighbours.append((cX, cY + dY))
        if not blocked(cX, cY, dX, 0, matrix):
            neighbours.append((cX + dX, cY))
        if (
            not blocked(cX, cY, 0, dY, matrix)
            or not blocked(cX, cY, dX, 0, matrix)
        ) and not blocked(cX, cY, dX, dY, matrix):
            neighbours.append((cX + dX, cY + dY))
        if blocked(cX, cY, -dX, 0, matrix) and not blocked(
            cX, cY, 0, dY, matrix
        ):
            neighbours.append((cX - dX, cY + dY))
        if blocked(cX, cY, 0, -dY, matrix) and not blocked(
            cX, cY, dX, 0, matrix
        ):
            neighbours.append((cX + dX, cY - dY))

    else:
        if dX == 0:
            if not blocked(cX, cY, dX, 0, matrix):
                if not blocked(cX, cY, 0, dY, matrix):
                    neighbours.append((cX, cY + dY))
                if blocked(cX, cY, 1, 0, matrix):
                    neighbours.append((cX + 1, cY + dY))
                if blocked(cX, cY, -1, 0, matrix):
                    neighbours.append((cX - 1, cY + dY))

        else:
            if not blocked(cX, cY, dX, 0, matrix):
                if not blocked(cX, cY, dX, 0, matrix):
                    neighbours.append((cX + dX, cY))
                if blocked(cX, cY, 0, 1, matrix):
                    neighbours.append((cX + dX, cY + 1))
                if blocked(cX, cY, 0, -1, matrix):
                    neighbours.append((cX + dX, cY - 1))
    return neighbours

def checkNeighbours(x, y, dir1, dir2, nextNodes):
    walls = []
    if not (m.sqrt(dir1**2 + dir2 ** 2), (x + dir1, y + dir2)) in nextNodes:
        walls.append(m.sqrt(dir1**2 + dir2 ** 2), (x + dir1, y + dir2))
    if dir1 == 0:
        if (m.sqrt(2), (x +1, y + dir2)) in nextNodes:
            walls.append((m.sqrt(2), (x +1, y + dir2)))
        if (m.sqrt(2), (x -1, y + dir2)) in nextNodes:
            walls.append((m.sqrt(2), (x -1, y + dir2)))
    elif dir2 == 0:
        if (m.sqrt(2), (x + dir1, y + 1)) in nextNodes:
            walls.append((m.sqrt(2), (x +dir1, y + 1)))
        if (m.sqrt(2), (x +dir1, y -1 )) in nextNodes:
            walls.append((m.sqrt(2), (x + dir1, y - 1)))
    else:
        if (m.sqrt(2), (x, y + dir2)) in nextNodes:
            walls.append((m.sqrt(2), (x, y + dir2)))
        if (m.sqrt(2), (x + dir1, y )) in nextNodes:
            walls.append((m.sqrt(2), (x + dir1, y)))
    return walls

def jump(cX, cY, dX, dY, matrix, goal):

    nX = cX + dX
    nY = cY + dY
    if blocked(nX, nY, 0, 0, matrix):
        return None

    if (nX, nY) == goal:
        return (nX, nY)

    oX = nX
    oY = nY

    if dX != 0 and dY != 0:
        while True:
            if (
                not blocked(oX, oY, -dX, dY, matrix)
                and blocked(oX, oY, -dX, 0, matrix)
                or not blocked(oX, oY, dX, -dY, matrix)
                and blocked(oX, oY, 0, -dY, matrix)
            ):
                return (oX, oY)

            if (
                jump(oX, oY, dX, 0, matrix, goal) != None
                or jump(oX, oY, 0, dY, matrix, goal) != None
            ):
                return (oX, oY)

            oX += dX
            oY += dY

            if blocked(oX, oY, 0, 0, matrix):
                return None

            if dblock(oX, oY, dX, dY, matrix):
                return None

            if (oX, oY) == goal:
                return (oX, oY)
    else:
        if dX != 0:
            while True:
                if (
                    not blocked(oX, nY, dX, 1, matrix)
                    and blocked(oX, nY, 0, 1, matrix)
                    or not blocked(oX, nY, dX, -1, matrix)
                    and blocked(oX, nY, 0, -1, matrix)
                ):
                    return (oX, nY)

                oX += dX

                if blocked(oX, nY, 0, 0, matrix):
                    return None

                if (oX, nY) == goal:
                    return (oX, nY)

        else:
            while True:
                if (
                    not blocked(nX, oY, 1, dY, matrix)
                    and blocked(nX, oY, 1, 0, matrix)
                    or not blocked(nX, oY, -1, dY, matrix)
                    and blocked(nX, oY, -1, 0, matrix)
                ):
                    return (nX, oY)

                oY += dY

                if blocked(nX, oY, 0, 0, matrix):
                    return None

                if (nX, oY) == goal:
                    return (nX, oY)

    return jump(nX, nY, dX, dY, matrix, goal)

def identifySuccessors(cX, cY, came_from, matrix, goal):
    successors = []
    neighbours = nodeNeighbours(cX, cY, came_from.get((cX, cY), 0), matrix)

    for cell in neighbours:
        dX = cell[0] - cX
        dY = cell[1] - cY

        jumpPoint = jump(cX, cY, dX, dY, matrix, goal)

        if jumpPoint != None:
            successors.append(jumpPoint)

    return successors

def lenght(current, jumppoint):
    dx, dy = direction(current[0], current[1], jumppoint[0], jumppoint[1])
    if dx != 0 and dy != 0:
        return m.sqrt(2) * abs(jumppoint[0] - current[0])
    else:
        return (abs(jumppoint[0] - current[0]) * abs(dx) + abs(jumppoint[1] - current[1]) * abs(dy)) * 1

def jps(start, goal, graphs):
    queue = []
    came_from = dict()
    cost_visited = {start: 0}
    heurustic_cost = {start: heurustic_func(start, goal)}
    close_set = set() 
    heappush(queue, (heurustic_cost[start], start))
    way = []
    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            way = []
            while cur_node in came_from:
                way.append(cur_node)
                cur_node = came_from[cur_node]
            way.append(start)
            way = way[::-1]
            return way
        close_set.add(cur_node)
        successors = identifySuccessors(cur_node[0], cur_node[1], came_from, graphs, goal)
        for jumpPoint in successors:
            if(jumpPoint in close_set):
                continue
            jpCost = cost_visited[cur_node] + lenght(cur_node, jumpPoint)
            
            if jpCost < cost_visited.get(jumpPoint, 0) or jumpPoint not in [el[1] for el in queue]:
                came_from[jumpPoint] = cur_node
                cost_visited[jumpPoint] = jpCost
                heurustic_cost[jumpPoint] = jpCost + heurustic_func(jumpPoint, goal)
                heappush(queue, (heurustic_cost[jumpPoint], jumpPoint))

    return way


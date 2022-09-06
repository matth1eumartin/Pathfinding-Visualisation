from calendar import c


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    c_2 = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    return c_2 ** 1/2

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
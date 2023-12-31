import itertools


def p1():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for s in d:
        if s.startswith('turn on'):
            _, _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] = 1
        elif s.startswith('turn off'):
            _, _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] = 0
        else:
            _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] ^= 1
    print(sum(sum(x) for x in grid))


def p2():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for s in d:
        if s.startswith('turn on'):
            _, _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] += 1
        elif s.startswith('turn off'):
            _, _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] = max(0, grid[y][x] - 1)
        else:
            _, c0, _, c1 = s.split(' ')
            x0, y0 = c0.split(',')
            x1, y1 = c1.split(',')
            for x, y in itertools.product(range(int(x0), int(x1)+1), range(int(y0), int(y1)+1)):
                grid[y][x] += 2
    print(sum(sum(x) for x in grid))


if __name__ == '__main__':
    p2()

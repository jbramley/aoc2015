def p1():
    with open("input", "r") as fp:
        d = fp.read()

    x, y = 0, 0
    h = {(0,0)}
    for c in d:
        if c == '^': y += 1
        elif c == 'v': y -= 1
        elif c == '>': x += 1
        elif c == '<': x -= 1
        h.add((x,y))
    print(len(h))


def p2():
    with open("input", "r") as fp:
        d = fp.read()

    h = {(0,0)}
    for s in (d[::2], d[1::2]):
        x, y = 0, 0
        for c in s:
            if c == '^': y += 1
            elif c == 'v': y -= 1
            elif c == '>': x += 1
            elif c == '<': x -= 1
            h.add((x,y))
    print(len(h))


if __name__ == '__main__':
    p2()

from collections import Counter


def p1():
    with open("input", "r") as fp:
        c = Counter(fp.read())
    print(c['(']-c[')'])


def p2():
    with open("input", "r") as fp:
        s = fp.read()
    f = 0
    for i, c in enumerate(s):
        f += 1 if c == '(' else -1
        if f < 0:
            print(i+1)
            return


if __name__ == '__main__':
    p2()

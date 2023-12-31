def p1():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    diff = 0
    for s in d:
        diff += len(s) - len(eval(s))  # really trusting AOC here

    print(diff)


def p2():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    diff = 0
    for s in d:
        diff += sum(1 for c in s if c in '\\"') + 2

    print(diff)


if __name__ == '__main__':
    p2()

def p1():
    with open("input", "r") as fp:
        d = fp.read().splitlines()
    t = 0
    for p in d:
        l, w, h = [int(c) for c in p.split("x")]
        a = 2*(l*w + w*h + l*h) + min(l*w, w*h, l*h)
        print(f"{p} -> 2*({l*w}+{w*h}+{l*h})+{min(l*w, w*h, l*h)} -> {a}")
        t += a
    print(t)


def p2():
    with open("input", "r") as fp:
        d = fp.read().splitlines()
    t = 0
    for p in d:
        l, w, h = [int(c) for c in p.split("x")]
        t += 2*(l+w+h-max(l, w, h)) + l*w*h
    print(t)


if __name__ == '__main__':
    p2()

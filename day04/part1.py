from hashlib import md5

INPUT = b'ckczppom'


def p1():
    h = md5(INPUT + b'0')
    i = 0
    while not h.hexdigest().startswith('00000'):
        i += 1
        h = md5(INPUT + bytes(str(i), 'utf8'))
    print(i)


def p2():
    h = md5(INPUT + b'0')
    i = 0
    while not h.hexdigest().startswith('000000'):
        i += 1
        h = md5(INPUT + bytes(str(i), 'utf8'))
    print(i)


if __name__ == '__main__':
    p2()

import itertools
from collections import defaultdict


def p1():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    nice = 0
    for s in d:
        has_double = False
        vowels = 0
        has_forbidden = False
        c0 = None
        for c in s:
            if c == c0:
                has_double = True
            if c in 'aeiou':
                vowels += 1
            if f"{c0}{c}" in ('ab', 'cd', 'pq', 'xy'):
                has_forbidden = True
            c0 = c
        if has_double and vowels >= 3 and not has_forbidden:
            nice += 1
    print(nice)


def p2():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    nice = 0
    for s in d:
        has_double = False
        has_triple = False
        ps = {}
        for i in range(len(s) - 1):
            if s[i:i+2] in ps:
                if ps[s[i:i+2]][0] != i -1:
                    has_double = True
                ps[s[i:i+2]].append(i)
            else:
                ps[s[i:i+2]] = [i]
            if i < len(s) - 2 and s[i] == s[i+2]:
                has_triple = True
        if has_double and has_triple:
            nice += 1
    print(nice)


if __name__ == '__main__':
    p2()

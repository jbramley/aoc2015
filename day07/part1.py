from collections import defaultdict, deque


class Gate:
    def __init__(self, out):
        self.inp = []
        self.out = out


class AndGate(Gate):
    def signal(self, val):
        if not self.inp:
            self.inp.append(val)
            return None
        else:
            return self.out, self.inp[0] & val


class OrGate(Gate):
    def signal(self, val):
        if not self.inp:
            self.inp.append(val)
            return None
        else:
            return self.out, self.inp[0] | val


class NotGate(Gate):
    def signal(self, val):
        return self.out, val ^ 65535


class YesGate(Gate):
    def signal(self, val):
        return self.out, val


class ShiftGate(Gate):
    def __init__(self, out, amt):
        super().__init__(out)
        self.amt = amt


class LshiftGate(ShiftGate):
    def signal(self, val):
        return self.out, (val << self.amt) & 65535


class RshiftGate(ShiftGate):
    def signal(self, val):
        return self.out, val >> self.amt


def p1():
    with open("input", "r") as fp:
        d = fp.read().splitlines()

    signals = deque()
    w = defaultdict(list)
    for n in d:
        inp, outp = n.split(" -> ")
        match inp.split(" "):
            case [in1, "AND", in2]:
                g = AndGate(outp)
                if in1.isnumeric():
                    g.signal(int(in1))
                else:
                    w[in1].append(g)
                w[in2].append(g)
            case [in1, "OR", in2]:
                g = OrGate(outp)
                w[in1].append(g)
                w[in2].append(g)
            case [in1, "LSHIFT", amt]:
                g = LshiftGate(outp, int(amt))
                w[in1].append(g)
            case [in1, "RSHIFT", amt]:
                g = RshiftGate(outp, int(amt))
                w[in1].append(g)
            case ["NOT", in1]:
                g = NotGate(outp)
                w[in1].append(g)
            case [val]:
                try:
                    signals.appendleft((outp, int(val)))
                except ValueError:
                    g = YesGate(outp)
                    w[val].append(g)

    while signals:
        o, v = signals.pop()
        if o not in w:
            print(f"Wire {o} has value {v}")
            continue
        for g in w[o]:
            r = g.signal(v)
            if r is not None:
                signals.appendleft(r)


if __name__ == '__main__':
    p1()

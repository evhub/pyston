class Random(object):
    def __init__(self, seed):
        self.cur = seed

    def __next__(self):
        self.cur = (self.cur * 1103515245 + 12345) % (1 << 31)
        return self.cur

def f():
    r = Random(0)
    t = 0
    for i in range(10000000):
        t = t + next(r)
    print(t)
f()

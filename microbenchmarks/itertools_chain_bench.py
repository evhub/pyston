# simple benchmark to test iteration over extension objects

import itertools

def f(c):
    for i in c:
        pass

l = []
r = list(range(500))
for i in range(100):
    l.append(itertools.chain(*[r for j in r]))
c = itertools.chain(*l)
f(c)

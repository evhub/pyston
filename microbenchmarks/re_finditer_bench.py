import re
def f():
    r = re.compile(" ")
    u = "a b c d"
    for i in range(2000000):
        r.finditer(u)
f()

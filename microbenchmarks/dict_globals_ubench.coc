d = dict(x=1, y=0)
exec("""
def g():
    global y
    y += x
""", d)

def f():
    g = d['g']
    for i in range(1000000):
        g()
        g()
        g()
        g()
        g()
        g()
        g()
        g()
        g()
        g()
        d['y'] += i
f()
print(d['y'])

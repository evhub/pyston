def sort(l):
    n = len(l)
    for i in range(n):
        print(i)
        for j in range(i):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l

l = []
N = 5000
for i in range(N):
    l.append(N - i)
sort(l)
print(l)

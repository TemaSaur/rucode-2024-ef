import sys
from collections import defaultdict as dd

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write


n, k = [int(x) for x in read().split()]

if k == (n * (n - 1) // 2):
    print(1, 1)
    exit()


graph = dd(set)

for i in range(k):
    a, b = [int(x) for x in read().split()]
    graph[a].add(b)
    graph[b].add(a)


from collections import deque


global_visited = set()
def bfs(graph, start):
    q = deque([start])
    visited = {start}
    while q:
        el = q.pop()
        visited.add(el)
        global_visited.add(el)
        for n in graph[el]:
            if n in visited:
                continue
            q.append(n)

    return visited


p = 0
for i in range(1, n + 1):
    if i in global_visited:
        continue
    component = bfs(graph, i)
    # print(component)
    l = len(component)
    p += (l * (l - 1)) // 2
        
from math import gcd

q = (n * (n - 1)) // 2

g = gcd(p, q)

p //= g
q //= g

print(p, q)
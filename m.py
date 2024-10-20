import sys
from collections import defaultdict as dd

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

A = {
    (8, 1, 8, 7),
    (2,),
    (11,),
    (7,),
    (6,),
    (3, 4),
    (17,),
    (8, 7),
    (5, 10),
}

for _ in range(int(read())):
    a = tuple([len(x) for x in read().split()])
    write("1\n" if a in A else "0\n")

import sys
from collections import defaultdict as dd

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

n = int(read())
tens = {10 ** i for i in range(6)}

ct = 0
l = 0
for i in range(1, n + 1):
    if i in tens:
        l += 1
        ct = 0
    if ct == 500:
        l += 1
        ct = 0
    ct += 1

write(f"{l}\n")
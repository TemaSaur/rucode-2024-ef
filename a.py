import sys
from collections import defaultdict as dd

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

n = int(read())

done = 1
res = 0
while done < n:
    done += 1
    res += 1
    mx = min(n, done + 499)

    if mx % 1000 == 0:
        mx  -= 1
    write(f"{mx}\n")
    
    res += len(str(mx)) - len(str(done))

write(f"{res}\n")

import sys
from collections import defaultdict as dd

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

struct = ['queue', 'stack']

res = ""
while res != "-1":
    print('get')
    res = input()
# input()

print('put 0\n')
# input()
print('put 1\n')
# input()
print('get')
res = input()
# print()

print("queue" if res == "0" else "stack")

# does not work

import sys
from collections import Counter

read = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

def main():
	# n = int(read())
	read()
	k = int(read())
	a = [int(x) for x in read().split()]
	b = [int(x) for x in read().split()]
	c = [int(x) for x in read().split()]

	A = [] * 4

	ct = Counter(a + b + c)

	c3 = 0
	total = 0
	for _, c_ in ct.most_common():
		if c_ == 3:
			total += 1
			k -= 1
		if c_ != 3:
			break

	if c3 >= k:
		write(f"{k}\n")
		return

	c2 = c1 = 0

	for A in [a, b, c]:
		c_ = 0
		for x in sorted(A, key=lambda w: -ct[w]):
			if c_ == k:
				break
			c_ += 1
			if ct[x] == 3:
				continue
			if ct[x] == 2:
				c2 += 1
				continue
			c1 += 1
	write(f"{c3 + c2 // 2 + c2 % 2 + c1}\n")


if __name__ == "__main__":
	main()


translate = {
	1000: "M",
	2000: "MM",
	3000: "MMM",
	100: "C",
	200: "CC",
	300: "CCC",
	400: "CD",
	500: "D",
	600: "DC",
	700: "DCC",
	800: "DCCC",
	900: "CM",
	10: "X",
	20: "XX",
	30: "XXX",
	40: "XL",
	50: "L",
	60: "LX",
	70: "LXX",
	80: "LXXX",
	90: "XC",
	1: "I",
	2: "II",
	3: "III",
	4: "IV",
	5: "V",
	6: "VI",
	7: "VII",
	8: "VIII",
	9: "IX",
	0: ""
}

prices = {
	"I": [1, 0, 0],
	"V": [0, 2, 0],
	"X": [0, 2, 0],
	"C": [0, 0, 1],
	"D": [1, 0, 1],
	"M": [2, 2, 0],
}

def rome(x):
	res = ""
	if x >= 1000:
		res = translate[x - x % 1000] + rome(x % 1000)
	elif x >= 100:
		res = translate[x - x % 100] + rome(x % 100)
	elif x >= 10:
		res = translate[x - x % 10] + rome(x % 10)
	else:
		return translate[x]

	return res

a = [[0, 0, 0, 0]]
for x in range(1, 4000):
	r = rome(x)
	if "L" in r:
		continue

	a0 = a1 = a2 = 0

	for c in r:
		a0 += prices[c][0]
		a1 += prices[c][1]
		a2 += prices[c][2]

	a.append([a0, a1, a2, a0 + a1 + a2, r])
print(a)	


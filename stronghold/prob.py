from math import log10

with open("rosalind_prob.txt", "r") as f:
    raw = f.read().splitlines()

s, a, b, at, gc = raw[0], raw[1].split(), [], 0, 0
for char in s:
    if char in ["A", "T"]:
        at += 1
    elif char in ["G", "C"]:
        gc += 1

for k in a:
    res = (gc * log10(float(k) / 2.0)) + (at * log10((1.0 - float(k))/ 2.0))
    b.append(str(round(res, 3)))

with open("output.txt", "w") as ff:
    ff.write(" ".join(b))

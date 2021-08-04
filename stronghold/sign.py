from itertools import permutations

with open("rosalind_sign.txt", "r") as ff:
    x = list(permutations(range(1, int(ff.read())+1)))
    ll = len(x[0])

s1 = [str(bin(i))[2:].replace("0", "-").replace("1", "+") for i in range(2 ** ll)]
s2 = ["-" * (ll - len(c)) + c for c in s1]
r = ""
lc = 0

for t in x:
    for s in s2:
        r += "\n" + " ".join([s[i] + str(t[i]) for i in range(len(s))]).replace("+", "")
        lc += 1

with open("output.txt", "w") as ff:
    ff.write(str(lc) + r)

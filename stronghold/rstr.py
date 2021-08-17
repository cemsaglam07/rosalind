with open("rosalind_rstr.txt", "r") as f:
    zzz = f.readline().split()
    n, gc = int(zzz[0]), float(zzz[1])
    s = f.readline().strip()
    at, prob = 1.0 - gc, 1.0

"""
zzz = input().split()
n, gc = int(zzz[0]), float(zzz[1])
s = input().strip()
at, prob = 1.0 - gc, 1.0
"""

for i in s:
    if i == "A" or i == "T":
        prob *= at / 2
    elif i == "G" or i == "C":
        prob *= gc / 2

print(1.0 - (1.0 - prob) ** n)

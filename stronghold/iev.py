# raw[0] = AA-AA => 100%
# raw[1] = AA-Aa => 100%
# raw[2] = AA-aa => 100%
# raw[3] = Aa-Aa => 75%
# raw[4] = Aa-aa => 50%
# raw[5] = aa-aa => 0%
p = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

with open("rosalind_iev.txt", "r") as f:
    raw = f.read().split()

c = 2  # No. of offsprings
sum = 0
for i, n in enumerate(raw):
    sum += (c * int(n) * p[i])
print(sum)

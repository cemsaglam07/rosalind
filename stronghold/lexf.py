from itertools import product

with open("rosalind_lexf.txt", "r") as f:
    data = f.read().splitlines()

cart = product(*[data[0].split() for i in range(int(data[1]))])
result = "\n".join(["".join(i) for i in cart])

with open("output.txt", "w") as ff:
    ff.write(result)

from helpers import fafsa
k = 4  # 4-mer as per instructions


def product(*args, repeat=k):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield "".join(prod)


d = {sub: "0" for sub in list(product("ACGT"))}
s = list(fafsa("rosalind_kmer.txt").values())[0]
for i in range(len(s)-k+1):
    d[s[i:i+k]] = str(int(d[s[i:i+k]]) + 1)
with open("output.txt", "w") as ff:
    ff.write(" ".join(list(d.values())))

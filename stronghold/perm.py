from itertools import permutations

with open("rosalind_perm.txt", "r") as ff:
    string = ff.read().splitlines()[0]

perm = [i for i in list(permutations([i + 1 for i in range(int(string))]))]
result = str(len(perm))
for i in range(len(perm)):
    tmp = "\n"
    for j in range(len(perm[i])):
        tmp += str(perm[i][j]) + " "
    result += tmp[:-1:]

with open("output.txt", "w") as f:
    f.write(result)

from helpers import fafsa

with open("stronghold/rosalind_mprt.txt", "r") as f:
    raw = f.read().splitlines()

files = ["http://www.uniprot.org/uniprot/" + i + ".fasta" for i in raw]
result = ""

for i, prt in enumerate(fafsa(*files).values()):
    loc = []
    for j in range(0, len(prt) - 3):
        if prt[j] == "N" and prt[j + 1] != "P" and prt[j + 2] in ["S", "T"] and prt[j + 3] != "P":
            loc.append(str(j + 1))
    if len(loc) > 0:
        result += files[i][31:-6] + "\n" + " ".join(loc) + "\n"

with open("output.txt", "w") as ff:
    ff.write(result.rstrip())

from helpers import dna_to_prot, fafsa, revc
import re


f = fafsa("rosalind_orf.txt")
table = dna_to_prot()

strings = []
for i in f.values():
    strings.append(i)
    strings.append(revc(i))

results = set()
for s in strings:
    for index in (m.start() for m in re.finditer('(?=ATG)', s)):
        sub = s[index:]

        # Check if there are stop codons
        if "TAG" not in sub and "TGA" not in sub and "TAA" not in sub:
            continue

        # Add open reading frames to a set
        # so that results won't be repeated
        orf = ""
        for i in range(0, (len(sub) // 3) * 3, 3):
            prot = table[sub[i:i+3]]
            if prot == "":
                results.add(orf)
                break
            orf += prot


with open("output.txt", "w") as ff:
    for i in results:
        print(i, file=ff)

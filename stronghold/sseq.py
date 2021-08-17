from helpers import fafsa
import re

data = fafsa("rosalind_sseq.txt")
s, t = data.values()
regex_t = "(" + ")(.*?)(".join(list(t)) + ")"

m = re.search(regex_t, s)
index = m.start()
count = 0

for i in m.groups():
    if count % 2 == 0:
        print(index + 1, end=" ")
    index += len(i)
    count += 1

with open("rosalind_grph.txt", "r") as f:
    raw = f.read().splitlines()

data = {}
tmp = ""
for item in raw:
    if len(item) > 0 and item[0] == ">":
        tmp = item[1:]
        data[tmp] = ""
    else:
        data[tmp] += item


def writeline(filename, string):
    with open(filename, "a+") as ff:
        ff.seek(0)
        if len(ff.read(100)) > 0:
            ff.write("\n")
        ff.write(string)


for s in data.keys():
    for t in data.keys():
        if data[s][-3:] == data[t][:3] and s != t:
            writeline("output.txt", s + " " + t)

with open("rosalind_ini5.txt", "r") as f:
    raw = f.read().splitlines()

raw = [raw[i] for i in range(1, len(raw), 2)]


def writeline(filename, string):
    with open(filename, "a+") as ff:
        ff.seek(0)
        if len(ff.read(100)) > 0:
            ff.write("\n")
        ff.write(string)


for item in raw:
    writeline("output.txt", item)

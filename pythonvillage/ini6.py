def writeline(filename, string):
    with open(filename, "a+") as ff:
        ff.seek(0)
        if len(ff.read(100)) > 0:
            ff.write("\n")
        ff.write(string)


with open("rosalind_ini6.txt", "r") as f:
    raw = f.read().splitlines()[0].split()

freq = {}
for word in raw:
    count = 0
    for item in raw:
        if word == item:
            count += 1
    freq[word] = count

for key, value in freq.items():
    writeline("output.txt", key + " " + str(value))

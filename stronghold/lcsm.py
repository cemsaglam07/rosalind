def fafsa():
    with open("rosalind_lcsm.txt", "r") as f:
        raw = f.read().splitlines()
    data = {}
    tmp = ""
    for item in raw:
        if len(item) > 0 and item[0] == ">":
            tmp = item[1:]
            data[tmp] = ""
        else:
            data[tmp] += item
    return data


def writeline(filename, string):
    with open(filename, "a+") as ff:
        ff.seek(0)
        if len(ff.read(100)) > 0:
            ff.write("\n")
        ff.write(string)

# Set data as a list of FAFSA values
data = list(fafsa().values())
# Set S as the shortest string in data
s = min(data, key=len)
# Store all substrings of L into a list
c = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
# Reverse sort them by their lengths
c.sort(key=len, reverse=True)
for sub in c:
    t = []
    for item in data:
        if item == s:
            continue
        t.append(item.find(sub))
    if int(-1) not in t:
        writeline("output.txt", sub)
        break

def fafsa():
    with open("rosalind_revp.txt", "r") as f:
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


def revc(x):
    string = str(x)[::-1]
    new = ""
    for char in string:
        if char == "A":
            new += "T"
        elif char == "T":
            new += "A"
        elif char == "C":
            new += "G"
        elif char == "G":
            new += "C"
    return new


result = ""
for key in fafsa().values():
    for i in range(len(key)):
        for j in range(i + 1, len(key) + 1):
            if len(key[i:j]) in range(4, 13):
                if key[i: j] == revc(key[i: j]):
                    result += str(i + 1) + " " + str(j - i) + "\n"

with open("output.txt", "w") as ff:
    ff.write(result.rstrip())

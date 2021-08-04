def fafsa():
    with open("rosalind_tran.txt", "r") as f:
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


s1, s2, rn, rd = list(fafsa().values())[0], list(fafsa().values())[1], 0, 0
for i in range(len(s1)):
    if s1[i] == s2[i]:
        continue
    elif s1[i] + s2[i] in ["AG", "GA", "CT", "TC"]:
        rn += 1
    else:
        rd += 1

print(rn / rd)

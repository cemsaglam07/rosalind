from math import factorial


def fafsa():
    with open("rosalind_pmch.txt", "r") as f:
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


d = list(fafsa().values())[0]
print(factorial(d.count("A")) * factorial(d.count("G")))

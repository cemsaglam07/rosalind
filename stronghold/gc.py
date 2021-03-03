with open("rosalind_gc.txt", "r") as f:
    raw = f.read().splitlines()

data = {}
tmp = ""
for item in raw:
    if len(item) > 0 and item[0] == ">":
        tmp = item
        data[tmp] = ["", ""]
    else:
        data[tmp][0] += item

for key, value in data.items():
    den = 0
    for char in value[0]:
        if char in ["G","C"]:
            den += 1
    data[key] = float(den) / len(value[0]) * 100

print(max(data, key=data.get)[1:])
print(data[max(data, key=data.get)])

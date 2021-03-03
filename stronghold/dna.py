string = str(input(""))
d = {"A": 0, "C": 0, "G": 0, "T": 0}
for char in string:
    d[char] += 1
string = str(d["A"]) + " " + str(d["C"]) + " " + str(d["G"]) + " " + str(d["T"])
print(string)

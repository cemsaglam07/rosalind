string = str(input(""))[::-1]
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
print(new)

s = str(input(""))
raw = [int(i) for i in str(input("")).split()]
print(s[raw[0]:raw[1]+1] + " " + s[raw[2]:raw[3]+1])

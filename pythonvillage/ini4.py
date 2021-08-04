raw = [int(i) for i in str(input("")).split()]
s = 0
for j in range(raw[0], raw[1] + 1):
    if j % 2 == 1:
        s += j
print(s)

with open("rosalind_mer.txt", "r") as f:
    data = f.read().splitlines()

n, a, m, b = int(data[0]), tuple(map(int, data[1].split())), int(data[2]), tuple(map(int, data[3].split()))

with open("rosalind_mer_output.txt", "w") as ff:
    x, y = 0, 0
    result = []
    while x < n and y < m:
        if a[x] < b[y]:
            result.append(a[x])
            x += 1
        else:
            result.append(b[y])
            y += 1

    if x < n:
        result.extend(a[x:])
    elif y < m:
        result.extend(b[y:])

print(*result, sep=" ")

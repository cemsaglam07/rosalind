with open("rosalind_mer.txt", "r") as f:
    data = f.read().splitlines()

n, a, m, b = int(data[0]), tuple(map(int, data[1].split())), int(data[2]), tuple(map(int, data[3].split()))

with open("rosalind_mer_output.txt", "w") as ff:
    x, y = 0, 0
    while x < n and y < m:
        if a[x] < b[y]:
            print(a[x], end=" ", file=ff)
            x += 1
        else:
            print(b[y], end=" ", file=ff)
            y += 1

    if x < n:
        print(*a[x:], file=ff)
    elif y < m:
        print(*b[y:], file=ff)

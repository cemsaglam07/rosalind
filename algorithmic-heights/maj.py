from collections import Counter

with open("rosalind_maj.txt", "r+") as f:
    data = f.read().splitlines()

n, m = data[0].split()
n, m = int(n), int(m) / 2

with open("rosalind_maj_output.txt", "w") as ff:
    for arr in data[1:n+1]:
        [(number, repeat)] = Counter(arr.split()).most_common(1)
        if repeat > m:
            print(number, end=" ", file=ff)
        else:
            print(-1, end=" ", file=ff)

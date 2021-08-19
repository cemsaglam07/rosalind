with open("rosalind_deg.txt", "r") as f:
    nm = f.readline().split()
    n, m = int(nm[0]), int(nm[1])

    edges = {k: set() for k in range(1, n+1)}

    for _ in range(m):
        xy = f.readline().split()
        x, y = int(xy[0]), int(xy[1])

        edges[x].add(y)
        edges[y].add(x)

with open("rosalind_deg_output.txt", "w") as ff:
    for k in sorted(edges):
        print(len(edges[k]), end=" ", file=ff)

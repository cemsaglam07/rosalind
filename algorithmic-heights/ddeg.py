with open("rosalind_ddeg.txt", "r") as f:
    nm = f.readline().split()
    n, m = int(nm[0]), int(nm[1])
    adj_list = {i: set() for i in range(1, n+1)}
    for _ in range(m):
        xy = f.readline().split()
        x, y = int(xy[0]), int(xy[1])
        adj_list[x].add(y)
        adj_list[y].add(x)


with open("rosalind_ddeg_output.txt", "w") as ff:
    for k in sorted(adj_list):
        neighbor_count = 0
        for nk in adj_list[k]:
            neighbor_count += len(adj_list[nk])
        print(neighbor_count, end=" ", file=ff)

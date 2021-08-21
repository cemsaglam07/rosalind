"""
Pseudocode of Breadth-First Search:

procedure BFS(G: graph, s: vertex):
    for all u in V do
        dist(u) = infinite

    dist(s) = 0
    Q: queue = [s]
    while Q is not empty do
        u = eject-from-front(Q)
        for all edges (u, v) in E do
            if dist(v) = Q then
                inject-to-end(Q, v)
                dist(v) = dist(u) + 1
"""


def bfs(adj, s):
    dist = {}
    for u in adj:
        dist[u] = -1

    dist[s] = 0
    queue = [s]
    while len(queue) > 0:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                queue.append(v)
                dist[v] = dist[u] + 1
    return dist


with open("rosalind_bfs.txt", "r") as f:
    nm = f.readline().split()
    n, m = int(nm[0]), int(nm[1])
    adj_list = {i: set() for i in range(1, n + 1)}
    for _ in range(m):
        xy = f.readline().split()
        adj_list[int(xy[0])].add(int(xy[1]))

with open("rosalind_bfs_output.txt", "w") as ff:
    for i in bfs(adj_list, 1).values():
        print(i, end=" ", file=ff)

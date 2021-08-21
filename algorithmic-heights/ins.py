with open("rosalind_ins.txt", "r") as f:
    n = int(f.readline())
    a = f.readline().split()
    a = [int(i) for i in a]

count = 0
for i in range(1, n):
    k = i
    while k > 0 and a[k] < a[k-1]:
        # swap a[k] and a[k-1]
        a[k], a[k-1] = a[k-1], a[k]
        count += 1
        k = k - 1

with open("rosalind_ins_output.txt", "w") as f:
    print(count, file=f)

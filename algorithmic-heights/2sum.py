with open("rosalind_2sum.txt", "r") as f:
    data = f.read().splitlines()


def negation(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == 0:
                return str(i + 1) + " " + str(j + 1)
    return -1


nm = data[0].split()
n, m = int(nm[0]), int(nm[1])
with open("rosalind_2sum_output.txt", "w") as ff:
    for arr in data[1:n+1]:
        arr = tuple(map(int, arr.split()[:m]))
        print(negation(arr), file=ff)

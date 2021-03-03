def fibd(n, m, k=1):
    data = [[0] * m] * n
    data[0] = [1] + data[0][1:]
    for i in range(1, n):
        data[i] = [k * sum(data[i - 1][1:m])] + data[i - 1][0:(m-1)]
    return sum(data[n - 1])


print(fibd(90, 20))

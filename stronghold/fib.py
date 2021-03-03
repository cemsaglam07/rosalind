def fib(n,k):
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, b + a * k
    return a

n_k = str(input("")).split()
print(fib(int(n_k[0]),int(n_k[1])))

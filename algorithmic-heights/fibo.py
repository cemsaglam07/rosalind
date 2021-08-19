def fibo(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x - 1) + fibo(x - 2)


with open("rosalind_fibo.txt", "r") as f:
    n = int(f.read())

with open("rosalind_fibo_output.txt", "w") as ff:
    print(fibo(n), file=ff)

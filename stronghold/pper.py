from math import factorial

with open("rosalind_pper.txt", "r") as ff:
    d = ff.read().split()
    n, k = int(d[0]), int(d[1])

# comb(n, k)! k=> n! / (k! * (n-k)!)
# perm(k) => k!
# partial perm  => comb(n,k) * perm(k)
#               => n! / (k! * (n-k)!) * k!
#               => n! / (n-k)!

print(int((factorial(n) / (factorial(n - k))) % 1000000))

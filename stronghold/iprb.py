def iprb(k,m,n):
    s = k + m + n

    # AA x AA = 100% dominant
    # AA x AA = 100% dominant
    # AA x AA = 100% dominant
    k1 = k / s

    # Aa x AA = 100% dominant
    # Aa x Aa = 75% dominant
    # Aa x aa = 50% dominant
    m1k2 = (m * k)
    m1m2 = (0.75 * m * (m-1))
    m1n2 = (0.5 * m * n)
    m1 = (m1k2 + m1m2 + m1n2) / (s * (s-1))

    # aa x AA = 100% dominant
    # aa x Aa = 50% dominant
    # aa x aa = 0% dominant
    n1k2 = (n * k)
    n1m2 = (0.5 * n * m)
    n1 = (n1k2 + n1m2) / (s * (s-1))

    return k1 + m1 + n1

user = [float(int(i)) for i in str(input(">>> ")).split()]
print(iprb(user[0], user[1], user[2]))

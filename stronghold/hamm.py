def hamm(s,t):
    dh = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dh += 1
    return dh

with open("rosalind_hamm.txt", "r") as f:
    raw = f.read().splitlines()

print(hamm(raw[0], raw[1]))

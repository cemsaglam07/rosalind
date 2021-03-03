def get_motifs():
    with open("rosalind_cons.txt", "r") as f:
        raw = f.read().splitlines()
    data = {}
    tmp = ""
    for item in raw:
        if len(item) > 0 and item[0] == ">":
            tmp = item
            data[tmp] = ""
        else:
            data[tmp] += item

    return list(data.values())

# Input:  A set of k-mers motifs
# Output: raw_profile(motifs)
def raw_profile(motifs):
    data = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        data[symbol] = []
        for j in range(k):
             data[symbol].append(0)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            data[symbol][j] += 1
    return data

# Input:  A set of k-mers motifs
# Output: A consensus string of motifs.
def consensus(motifs):
    k = len(motifs[0])
    p = raw_profile(motifs)
    string = ""
    for j in range(k):
        m = 0
        frequentsymbol = ""
        for symbol in "ACGT":
            if p[symbol][j] > m:
                m = p[symbol][j]
                frequentsymbol = symbol
        string += frequentsymbol
    return string

# Pretty prints raw_profile
def profile(motifs):
    motifs = raw_profile(motifs)
    key_list = list(motifs.keys())
    for i in [{k: motifs[k]} for k in key_list]:
        string = repr(i)
        string = string.replace("{", "")
        string = string.replace("}", "")
        string = string.replace("'", "")
        string = string.replace(",", "")
        string = string.replace("[", "")
        string = string.replace("]", "")
        print(string)

def main():
    motifs = get_motifs()
    print(consensus(motifs))
    profile(motifs)

main()

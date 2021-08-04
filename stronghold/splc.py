table = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F",
         "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I",
         "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S",
         "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T",
         "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S",
         "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
         "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "CAA": "Q",
         "AAA": "K", "GAA": "E", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C",
         "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S",
         "GGC": "G", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R",
         "AGG": "R", "GGG": "G", "UGA": "", "UAA": "", "UAG": ""}


def fafsa():
    with open("rosalind_splc.txt", "r") as f:
        raw = f.read().splitlines()
    data = {}
    tmp = ""
    for item in raw:
        if len(item) > 0 and item[0] == ">":
            tmp = item[1:]
            data[tmp] = ""
        else:
            data[tmp] += item
    return data


# Remove introns from DNA string
string = max(fafsa().values(), key=len)
subs = [i for i in fafsa().values() if i != string]
for i in range(len(subs)):
    string = string.replace(subs[i], "")

# Convert DNA into RNA
string = string.replace("T", "U")

# Convert RNA to protein string
result = ""
for i in range(0, len(string), 3):
    result += table[string[i:i + 3]]

with open("output.txt", "w") as ff:
    ff.write(result)

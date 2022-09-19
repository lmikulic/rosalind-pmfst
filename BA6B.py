def drugacijiZapis(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return [0] + tmp + [len(tmp) + 1]

def n_breakpoints(permutation):
    return len(permutation) - 1 - n_adjacencies(permutation)

def n_adjacencies(permutation):
    count = 0
    for i in range(len(permutation) - 1):
        count += is_adjacency((permutation[i], permutation[i + 1]))
    return count

def is_adjacency(pair):
    if pair[1] - pair[0] == 1:
        return 1
    return 0

if __name__=="__main__":
    with open("../Downloads/rosalind_ba6b.txt", "r") as f:
        permutacija=[line.strip() for line in f.readlines()]
    permutacija2=drugacijiZapis(permutacija[0])
    rezultat= n_breakpoints(permutacija2)
    print(rezultat)

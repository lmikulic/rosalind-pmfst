def Text(kmers):
    text=kmers[0]
    for i in range(1, len(kmers)):
        kmer=kmers[i]
        text=text+kmer[(len(kmer)-1)]
    return text

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3b.txt", "r") as f:
        kmers=[line.strip() for line in f.readlines()]
    rezultat=Text(kmers)
    print(rezultat)

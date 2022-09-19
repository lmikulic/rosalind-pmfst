def Overlap(kmers):
    overlap=[]
    kmers.sort()
    for i in range(0, len(kmers)):
        kmer1=kmers[i]
        for j in range(0, len(kmers)):
            if(i!=j):
                kmer2=kmers[j]
                if((kmer1[1:(len(kmer1))])==(kmer2[0:(len(kmer2)-1)])):
                    overlap.append(kmer1 + " -> " + kmer2)
    return overlap        
        
if __name__=="__main__":
    with open("../Downloads/rosalind_ba3c.txt", "r") as f:
        kmers=[line.strip() for line in f.readlines()]
    rezultat=Overlap(kmers)
    for element in rezultat:
        print(element)

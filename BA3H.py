def string_reconstruction(k,kmers):
    prefiksi=[]
    sufiksi=[]
    D=dict()

    for kmer in kmers:
        prefiksi.append(kmer[:-1])
        sufiksi.append(kmer[1:])
        D[kmer[:-1]]=kmer[k-1]

    for p in prefiksi:
        if(p not in sufiksi):
            pocetni_prefiks=p

    for s in sufiksi:
        if(s not in prefiksi):
            zadnji_sufiks=s

    tekst=pocetni_prefiks+D[pocetni_prefiks]

    while True:
        if(tekst[len(tekst)-k+1:]==zadnji_sufiks):
            break
        else:
            tekst=tekst+D[tekst[len(tekst)-k+1:]]

    return tekst
        

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3h.txt","r") as f:
        k=int(f.readline())
        kmers=[line.strip() for line in f.readlines()]
    rezultat=string_reconstruction(k,kmers)
    print(rezultat)

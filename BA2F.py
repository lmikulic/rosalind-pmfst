import random

def getKmers(text, k):
    kmers=set()
    duljina=len(text)
    for i in range(0, len(text)-k+1):
        kmers.add(text[i:(i+k)])
    return kmers

def randomKmers(Dna, k):
    Motifs=[]
    duljina=len(Dna[0])
    for el in Dna:
        n=random.randint(0, duljina-k)
        kmer=el[n:(n+k)]
        Motifs.append(kmer)
    return Motifs

def createProfileMatrix(Dna, pseudocounts=False):
    duljina=len(Dna[0])
    profile=dict()

    profile["A"]=[0]*k
    profile["C"]=[0]*k
    profile["G"]=[0]*k
    profile["T"]=[0]*k

    for el in Dna:
        for x in enumerate(el):
            profile[x[1]][x[0]]=profile[x[1]][x[0]]+1

    if(pseudocounts):
        profile["A"]=[x+1 for x in profile["A"]]
        profile["C"]=[x+1 for x in profile["C"]]
        profile["G"]=[x+1 for x in profile["G"]]
        profile["T"]=[x+1 for x in profile["T"]]

    for i in range(0, k):
        zbroj=profile["A"][i]+profile["C"][i]+profile["G"][i]+profile["T"][i]
        profile["A"][i]=(profile["A"][i])/zbroj
        profile["C"][i]=(profile["C"][i])/zbroj
        profile["G"][i]=(profile["G"][i])/zbroj
        profile["T"][i]=(profile["T"][i])/zbroj

    return profile

def Vjerojatnost(pattern, profile):
    p=1
    for x in enumerate(pattern):
        p=p*(profile[x[1]][x[0]])
    return p

def profileMostProbable(text, k, profile):
    kmers=getKmers(text, k)
    najvjv_kmer=""
    najvjv=-1
    for kmer in kmers:
        vjv=Vjerojatnost(kmer, profile)
        if(vjv>najvjv):
            najvjv_kmer=kmer
            najvjv=vjv
    return najvjv_kmer

def getMotifs(Dna, profile, k):
    Motifs=[]
    for el in Dna:
        Motifs.append(profileMostProbable(el, k, profile))
    return Motifs

def score(motifs):
    zip1=zip(*motifs)

    najveci=[]

    for x in zip1:
        brojA=sum([y=="A" for y in x])
        brojC=sum([y=="C" for y in x])
        brojG=sum([y=="G" for y in x])
        brojT=sum([y=="T" for y in x])
        najveci.append(len(motifs)-max(brojA, brojC, brojG, brojT))

    zbroj=sum(najveci)
    return zbroj

def randomizedMotifSearchAtom(Dna, k):
    motifs=randomKmers(Dna, k)
    bestMotifs=motifs

    while(True):
        profile=createProfileMatrix(motifs, pseudocounts=True)
        motifs=getMotifs(Dna, profile, k)
        if(score(motifs)<score(bestMotifs)):
            bestMotifs=motifs
        else:
            return bestMotifs

def randomizedMotifSearch(Dna, k):
    bestMotifs=randomizedMotifSearchAtom(Dna, k)
    for i in range(0, 1000):
        motifs=randomizedMotifSearchAtom(Dna, k)
        if(score(motifs)<score(bestMotifs)):
            bestMotifs=motifs
    return bestMotifs

    
if __name__=="__main__":
    with open("../Downloads/rosalind_ba2f(2).txt", "r") as f:
        k,t=map(int, f.readline().strip().split())
        Dna=[line.strip() for line in f.readlines()]
    rezultat=randomizedMotifSearch(Dna, k)
    for element in rezultat:
        print(element)

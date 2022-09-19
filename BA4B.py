Text=input("Text: ")
Peptide=input("Peptide: ")

codon=["AAA", "CAA", "GAA", "UAA", "AAC", "CAC", "GAC", "UAC" ,"AAG",   "CAG",   "GAG",   "UAG" ,"AAU",   "CAU",   "GAU",   "UAU", 
 "ACA",   "CCA",   "GCA",   "UCA","ACC",   "CCC",   "GCC",   "UCC", "ACG",   "CCG",   "GCG",   "UCG", "ACU",   "CCU",   "GCU",   "UCU", 
 "AGA",   "CGA",   "GGA",   "UGA", "AGC",   "CGC",   "GGC",   "UGC", "AGG",   "CGG",   "GGG",   "UGG", 
 "AGU",   "CGU",   "GGU",   "UGU", "AUA",   "CUA",   "GUA",   "UUA", "AUC",   "CUC",   "GUC",   "UUC", 
 "AUG",   "CUG",   "GUG",   "UUG", "AUU",   "CUU",   "GUU",   "UUU"]

aminoacid=["K", "Q",  "E", "","N", "H",  "D", "Y","K", "Q" , "E", "","N", "H",  "D", "Y","T", "P",  "A", "S","T", "P" , "A", "S",
"T", "P",  "A", "S","T", "P" , "A" ,"S","R", "R" , "G", "","S", "R",  "G", "C","R", "R",  "G", "W","S", "R",  "G", "C",
"I", "L",  "V", "L","I", "L" , "V", "F","M", "L" ,"V", "L","I", "L", "V", "F"]


def reverseComplement(podniz):
    k=len(podniz)-1

    Rezultat=""

    while(k>=0):
        if(podniz[k]=="A"):
            Rezultat=Rezultat+"T"
        if(podniz[k]=="T"):
            Rezultat=Rezultat+"A"
        if(podniz[k]=="C"):
            Rezultat=Rezultat+"G"
        if(podniz[k]=="G"):
            Rezultat=Rezultat+"C"
        k=k-1

    return Rezultat

def rna(podniz):
    k=0

    Rezultat=""

    while(k<len(podniz)):
        if(podniz[k]=="A"):
            Rezultat=Rezultat+"A"
        if(podniz[k]=="T"):
            Rezultat=Rezultat+"U"
        if(podniz[k]=="C"):
            Rezultat=Rezultat+"C"
        if(podniz[k]=="G"):
            Rezultat=Rezultat+"G"
        k=k+1

    return Rezultat

def  aminoAcidSequence(podniz):
    rezultat=""

    i=0

    while i<=(len(podniz)-3):
        kmer=podniz[i:i+3]
        for j in range(0, 64):
            if(kmer==codon[j]):
                rezultat=rezultat+aminoacid[j]
                break
        i=i+3
    return rezultat
        

duljina=len(Peptide)

podnizovi=[]
f=0

for i in range(0, len(Text)-(3*duljina)+1):
    podniz1=Text[i:(i+3*duljina)]
    podniz1_glavni=rna(podniz1)
    if(aminoAcidSequence(podniz1_glavni)==Peptide):
        podnizovi.append(podniz1)
        f=1
    if(f==0):
        podniz2=reverseComplement(podniz1)
        podniz2_glavni=rna(podniz2)
        if(aminoAcidSequence(podniz2_glavni)==Peptide):
            podnizovi.append(podniz1)
    f=0
    

for podniz in podnizovi:
    print(podniz)

Pattern=input("Pattern: ")

codon=["AAA", "CAA", "GAA", "UAA", "AAC", "CAC", "GAC", "UAC" ,"AAG",   "CAG",   "GAG",   "UAG" ,"AAU",   "CAU",   "GAU",   "UAU", 
 "ACA",   "CCA",   "GCA",   "UCA","ACC",   "CCC",   "GCC",   "UCC", "ACG",   "CCG",   "GCG",   "UCG", "ACU",   "CCU",   "GCU",   "UCU", 
 "AGA",   "CGA",   "GGA",   "UGA", "AGC",   "CGC",   "GGC",   "UGC", "AGG",   "CGG",   "GGG",   "UGG", 
 "AGU",   "CGU",   "GGU",   "UGU", "AUA",   "CUA",   "GUA",   "UUA", "AUC",   "CUC",   "GUC",   "UUC", 
 "AUG",   "CUG",   "GUG",   "UUG", "AUU",   "CUU",   "GUU",   "UUU"]

aminoacid=["K", "Q",  "E", "","N", "H",  "D", "Y","K", "Q" , "E", "","N", "H",  "D", "Y","T", "P",  "A", "S","T", "P" , "A", "S",
"T", "P",  "A", "S","T", "P" , "A" ,"S","R", "R" , "G", "","S", "R",  "G", "C","R", "R",  "G", "W","S", "R",  "G", "C",
"I", "L",  "V", "L","I", "L" , "V", "F","M", "L" ,"V", "L","I", "L", "V", "F"]

rezultat=""

i=0

while i<=(len(Pattern)-3):
    kmer=Pattern[i:i+3]
    for j in range(0, 64):
        if(kmer==codon[j]):
            rezultat=rezultat+aminoacid[j]
            break
    i=i+3

print(rezultat)

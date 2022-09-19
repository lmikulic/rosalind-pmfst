def HammingDistance(Pattern1, Pattern2):
    broj=0

    for i in range(0, len(Pattern1)):
        if((Pattern1[i])!=(Pattern2[i])):
            broj=broj+1
    return broj
    

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k=len(Pattern)
    distance=0
    for el in Dna:
        Hamming_Distance=k
        for i in range(0, len(el)-k+1):
            Pattern2=el[i:(i+k)]
            if(Hamming_Distance>(HammingDistance(Pattern, Pattern2))):
                Hamming_Distance=(HammingDistance(Pattern, Pattern2))
        distance=(distance+Hamming_Distance)
    return distance

Pattern=input("Upisite pattern: ")
Dna=input("Dna: ")
Dna=Dna.split()

print(DistanceBetweenPatternAndStrings(Pattern, Dna))

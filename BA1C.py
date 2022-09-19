Pattern=input("Pattern: ")

k=len(Pattern)-1

Rezultat=""

while(k>=0):
    if(Pattern[k]=="A"):
        Rezultat=Rezultat+"T"
    if(Pattern[k]=="T"):
        Rezultat=Rezultat+"A"
    if(Pattern[k]=="C"):
        Rezultat=Rezultat+"G"
    if(Pattern[k]=="G"):
        Rezultat=Rezultat+"C"
    k=k-1

print(Rezultat)

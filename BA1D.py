Pattern=input("Pattern: ")
Genome=input("Genome: ")

k=len(Genome)
l=len(Pattern)

for i in range(0,k-l+1):
    if(Genome[i:i+l]==Pattern):
        print(i, end=" ")

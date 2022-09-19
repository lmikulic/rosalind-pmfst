text=input("Text: ")
k=input("k: ")
k=int(k)

d=input("d: ")
d=int(d)

lista_k=["A", "T", "G", "C"]

broj=0

for el in lista_k:
    broj=broj+1

duljina=len(lista_k[0])

while(duljina<k):
    for i in range(0, broj):
        lista_k.append(lista_k[i]+"T")
        lista_k.append(lista_k[i]+"G")
        lista_k.append(lista_k[i]+"C")
        lista_k[i]=lista_k[i]+"A"
    broj=0
    for element in lista_k:
        broj=broj+1
    duljina=len(lista_k[0])

lista_brojeva=[]

for m in range(0, broj):
    Pattern1=lista_k[m]
    dulj=len(Pattern1)-1
    reverse_complement=""

    while(dulj>=0):
        if(Pattern1[dulj]=="A"):
            reverse_complement=reverse_complement+"T"
        if(Pattern1[dulj]=="T"):
            reverse_complement=reverse_complement+"A"
        if(Pattern1[dulj]=="C"):
            reverse_complement=reverse_complement+"G"
        if(Pattern1[dulj]=="G"):
            reverse_complement=reverse_complement+"C"
        dulj=dulj-1

    ukupno1=0
    for n in range(0, len(text)-k+1):
        Pattern2=text[n:n+k]
        brojd1=0
        for o in range(0, k):
            if(Pattern1[o]!=Pattern2[o]):
                brojd1=brojd1+1
        if(brojd1<=d):
            ukupno1=ukupno1+1

    ukupno2=0
    for t in range(0, len(text)-k+1):
        Pattern2=text[t:t+k]
        brojd2=0
        for z in range(0, k):
            if(reverse_complement[z]!=Pattern2[z]):
                brojd2=brojd2+1
        if(brojd2<=d):
            ukupno2=ukupno2+1
    
    lista_brojeva.append(ukupno1+ukupno2)

najveci=lista_brojeva[0]

for br in lista_brojeva:
    if(br>najveci):
        najveci=br

for p in range(0, broj):
    if(lista_brojeva[p]==najveci):
        print(lista_k[p], end=' ')

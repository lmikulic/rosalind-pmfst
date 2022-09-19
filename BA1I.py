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
    ukupno=0
    for n in range(0, len(text)-k+1):
        Pattern2=text[n:n+k]
        brojd=0
        for o in range(0, k):
            if(Pattern1[o]!=Pattern2[o]):
                brojd=brojd+1
        if(brojd<=d):
            ukupno=ukupno+1
    lista_brojeva.append(ukupno)

najveci=lista_brojeva[0]

for br in lista_brojeva:
    if(br>najveci):
        najveci=br

for p in range(0, broj):
    if(lista_brojeva[p]==najveci):
        print(lista_k[p], end=' ')

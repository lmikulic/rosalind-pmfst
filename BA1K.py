text=input("Text: ")
k=input("k: ")
k=int(k)

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

lista_k.sort()

lista_brojeva=[]

for m in range(0, broj):
    Pattern1=lista_k[m]
    ukupno=0
    for n in range(0, len(text)-k+1):
        Pattern2=text[n:n+k]
        if(Pattern1==Pattern2):
            ukupno=ukupno+1
    lista_brojeva.append(ukupno)

rezultat=""

for br in lista_brojeva:
    rezultat=rezultat+str(br)+" "

print(rezultat)

f=0

while(f==0):
    glavni_broj=input("Koliko ćete stringova upisati? ")
    glavni_broj=int(glavni_broj)
    if(glavni_broj!=0):
        f=1

stringovi=[]

string1=input("Upisite string: ")
stringovi.append(string1)
duljina=len(string1)

for i in range(0, glavni_broj-1):
    string2=input("Upisite string: ")
    while(len(string2)!=duljina):
        string2=input("Upisite string: ")
    stringovi.append(string2)

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

glavna_lista=[]

for j in range(0, broj):
    pattern1=lista_k[j]
    lista_d=[]
    br_sadrzi=0
    for m in range(0, broj):
        broj1=0
        pattern2=lista_k[m]
        for l in range(0, k):
            if(pattern1[l]!=pattern2[l]):
                broj1=broj1+1
        if(broj1<=d):
            lista_d.append(pattern2)
    for n in range(0, glavni_broj):
        for elem in lista_d:
            if(elem in stringovi[n]):
                br_sadrzi=br_sadrzi+1
                break
    if(br_sadrzi==glavni_broj):
        glavna_lista.append(pattern1)
    
for glavni in glavna_lista:
    print(glavni, end=" ")

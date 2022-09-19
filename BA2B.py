k=input("k: ")
k=int(k)
def d1(Pattern, Text):
    duljinaPattern=len(Pattern)
    duljinaText=len(Text)
    brojevi=[]
    for i in range(0, duljinaText-duljinaPattern+1):
        pattern2=Text[i:i+duljinaPattern]
        broj_razlicitih=0
        for j in range(0, duljinaPattern):
            if(Pattern[j]!=pattern2[j]):
                broj_razlicitih=broj_razlicitih+1
        brojevi.append(broj_razlicitih)
    mini=brojevi[0]
    for br in brojevi:
        if(br<mini):
            mini=br
    return mini   

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

zavrsni_brojevi=[]

for m in range(0, broj):
    Pattern=lista_k[m]
    Pattern_Dna=d1(Pattern, string1)
    for n in range(1, glavni_broj):
        Pattern_Dna=Pattern_Dna+d1(Pattern, stringovi[n])
    zavrsni_brojevi.append(Pattern_Dna)

mini_glavni=zavrsni_brojevi[0]
index_glavni=0

for p in range(1, broj):
    if(zavrsni_brojevi[p]<mini_glavni):
        mini_glavni=zavrsni_brojevi[p]
        index_glavni=p

print(lista_k[index_glavni])

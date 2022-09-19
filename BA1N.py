Pattern=input("Pattern: ")
d=input("d: ")
d=int(d)

k=len(Pattern)

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

lista=[]

def Razlika(string1, string2, d1):
    broj1=0
    for i in range(0, k):
        if(string1[i]!=string2[i]):
            broj1=broj1+1
    if(broj1<=d1):
        return True
    else:
        return False
    
for j in range(0, broj):
    if(Razlika(Pattern, lista_k[j], d)):
        lista.append(lista_k[j])

for element in lista:
    print(element)

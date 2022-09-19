Pattern=input("Unesite pattern: ")
Text=input("Unesite text: ")
d=input("Unesite d: ")
d=int(d)

lista_pozicija=[]

duljina_pattern=len(Pattern)

for i in range(0, len(Text)-duljina_pattern+1):
    Pattern2=Text[i:i+duljina_pattern]
    broj=0
    for j in range(0, duljina_pattern):
        if(Pattern[j]!=Pattern2[j]):
            broj=broj+1
    if(broj<=d):
        lista_pozicija.append(i)

rezultat=""

for el in lista_pozicija:
    rezultat=rezultat+str(el)+" "
            
print(rezultat)

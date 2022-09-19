k=input("k: ")
k=int(k)

Text=input("Text: ")

niz1=[]

k1=k-1

for i in range(0, len(Text)-k1):
    niz1.append(Text[i:(i+k1)]+" -> "+Text[(i+1):(i+1+k1)])
    
dodatni_pozicija=[]

for j in range(0, len(Text)-k1-1):
    for l in range(j+1, len(Text)-k1):
        if(((niz1[j])[0:k1])==((niz1[l])[0:k1])):
            (niz1[j])=(niz1[j])+","+(niz1[l])[(k1+4):(2*k1+4)]
            dodatni_pozicija.append(l)

dodatni_pozicija2=[]

for element in dodatni_pozicija:
    if(dodatni_pozicija2.count(element)==0):
        dodatni_pozicija2.append(element)

dodatni_pozicija2.sort()

duljina=len(dodatni_pozicija2)
while(duljina>0):
    niz1.pop(dodatni_pozicija2[duljina-1])
    duljina=duljina-1

for el in niz1:
    print(el)

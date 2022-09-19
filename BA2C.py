Text=input("Text: ")

k=input("k: ")
k=int(k)

prvi_red=input("Unesite prvi red matrice Profile: ")
drugi_red=input("Unesite drugi red matrice Profile: ")
treci_red=input("Unesite treci red matrice Profile: ")
cetvrti_red=input("Unesite cetvrti red matrice Profile: ")

vjerojatnosti1=[]
broj_vj=0
vjerojatnosti1.append("")

for i in range(0, len(prvi_red)):
    if(prvi_red[i]!=" "):
        vjerojatnosti1[broj_vj]=vjerojatnosti1[broj_vj]+prvi_red[i]
    if(prvi_red[i]==" "):
        broj_vj=broj_vj+1
        vjerojatnosti1.append("")

vjerojatnosti2=[]
broj_vj=0
vjerojatnosti2.append("")

for i in range(0, len(drugi_red)):
    if(drugi_red[i]!=" "):
        vjerojatnosti2[broj_vj]=vjerojatnosti2[broj_vj]+drugi_red[i]
    if(drugi_red[i]==" "):
        broj_vj=broj_vj+1
        vjerojatnosti2.append("")

vjerojatnosti3=[]
broj_vj=0
vjerojatnosti3.append("")

for i in range(0, len(treci_red)):
    if(treci_red[i]!=" "):
        vjerojatnosti3[broj_vj]=vjerojatnosti3[broj_vj]+treci_red[i]
    if(treci_red[i]==" "):
        broj_vj=broj_vj+1
        vjerojatnosti3.append("")

vjerojatnosti4=[]
broj_vj=0
vjerojatnosti4.append("")

for i in range(0, len(cetvrti_red)):
    if(cetvrti_red[i]!=" "):
        vjerojatnosti4[broj_vj]=vjerojatnosti4[broj_vj]+cetvrti_red[i]
    if(cetvrti_red[i]==" "):
        broj_vj=broj_vj+1
        vjerojatnosti4.append("")

for j in range(0, k):
    vjerojatnosti1[j]=float(vjerojatnosti1[j])
    vjerojatnosti2[j]=float(vjerojatnosti2[j])
    vjerojatnosti3[j]=float(vjerojatnosti3[j])
    vjerojatnosti4[j]=float(vjerojatnosti4[j])    

lista_k=[]

for r in range(0, len(Text)-k+1):
    lista_k.append(Text[r:r+k])

broj=0
for elem in lista_k:
    broj=broj+1

vjerojatnosti_glavne=[]

for t in range(0, broj):
    p=lista_k[t]
    produkt=1
    for n in range(0, k):
        if(p[n]=="A"):
            produkt=produkt*vjerojatnosti1[n]
        if(p[n]=="C"):
            produkt=produkt*vjerojatnosti2[n]
        if(p[n]=="G"):
            produkt=produkt*vjerojatnosti3[n]
        if(p[n]=="T"):
            produkt=produkt*vjerojatnosti4[n]
    vjerojatnosti_glavne.append(produkt)

maxi=vjerojatnosti_glavne[0]
index_glavni=0

for d in range(0, broj):
    if(vjerojatnosti_glavne[d]>maxi):
        maxi=vjerojatnosti_glavne[d]
        index_glavni=d

print(lista_k[index_glavni])

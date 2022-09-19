Text=input("Text: ")
k=input("k: ")
k=int(k)

l=len(Text)

Lista=[]
Lista_brojeva=[]

for i in range(0,l-k+1):
    Lista.append(Text[i:i+k])
    Lista_brojeva.append(0)
    
for j in range(0,l-k+1):
    for element in Lista:
        if(Lista[j]==element):
            Lista_brojeva[j]=Lista_brojeva[j]+1

najvise=0

Lista_najvise1=[]

for element2 in Lista_brojeva:
    if(element2>najvise):
        najvise=element2

for k in range(0,l-k+1):
    if(Lista_brojeva[k]==najvise):
        Lista_najvise1.append(Lista[k])

m=0
Lista_najvise=[]

for el in Lista_najvise1:
    m=m+1

for o in range(0,m):
    f=0
    for p in range(0,o):
        if(Lista_najvise1[o]==Lista_najvise1[p]):
            f=f+1
    if(f==0):
        Lista_najvise.append(Lista_najvise1[o])

for elementi in Lista_najvise:
    print(elementi, end=" ")

k=input("k: ")
k=int(k)

Text=input("Text: ")

Composition=[]

for i in range(0, len(Text)-k+1):
    Composition.append(Text[i:(i+k)])

Composition.sort()

for el in Composition:
    print(el)

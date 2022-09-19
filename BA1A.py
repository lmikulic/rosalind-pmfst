Text=input("Text: ")
Pattern=input("Pattern: ")

l=len(Text)
k=len(Pattern)

Lista=[]

for i in range(0,l-k+1):
    Lista.append(Text[i:i+k])

broj=0

for element in Lista:
    if(element==Pattern):
        broj=broj+1

print(broj)

def NumberToSymbol(index):
    if(index==0):
        index="A"
    if(index==1):
        index="C"
    if(index==2):
        index="G"
    if(index==3):
        index="T"
    return index

def NumberToPattern(index, k):
    if(k==1):
        return NumberToSymbol(index)
    prefixIndex=index//4
    r=index%4
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixIndex, k-1)
    return PrefixPattern+symbol

index=input("index: ")
index=int(index)

k=input("k: ")
k=int(k)

print(NumberToPattern(index, k))

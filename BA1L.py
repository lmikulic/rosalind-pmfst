def SymbolToNumber(symbol):
    if(symbol=="A"):
        symbol=0
    if(symbol=="C"):
        symbol=1
    if(symbol=="G"):
        symbol=2
    if(symbol=="T"):
        symbol=3
    return symbol

def PatternToNumber(Pattern):
    if(len(Pattern)==0):
        return 0
    symbol=Pattern[len(Pattern)-1]
    Prefix=Pattern[0:len(Pattern)-1]
    return 4*PatternToNumber(Prefix)+SymbolToNumber(symbol)

Pattern=input("Pattern: ")
print(PatternToNumber(Pattern))

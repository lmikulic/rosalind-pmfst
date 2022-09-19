string1=input("Upisite prvi string: ")
duljina1=len(string1)

string2=input("Upisite drugi string: ")
duljina2=len(string2)

while(duljina2!=duljina1):
    string2=input("Upisite drugi string: ")
    duljina2=len(string2)

broj=0

for i in range(0, duljina1):
    if(string1[i]!=string2[i]):
        broj=broj+1

print(broj)

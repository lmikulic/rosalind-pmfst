def debrujin(niz):
    D=dict()
    for prvi, drugi in niz:
        D[(prvi[:-1],drugi[:-1])]=(prvi[1:],drugi[1:])
    return D

def eulerian_path(D):
    keys=list(D.keys())
    values=list(D.values())

    for i in range(len(keys)):
        if(keys[i] not in values):
            prvi=keys[i]

    for i in range(len(values)):
        if(values[i] not in keys):
            zadnji=values[i]

    for i in range(len(keys)):
        if(keys[i]==prvi):
            indeks=i

    par=values[indeks]

    put=[prvi,par]

    while(par!=zadnji):
        for i in range(0,len(keys)):
            if(keys[i]==par):
                put.append(values[i])
                par=values[i]

    return put

def string_spelled_gapped_patterns(path,k,d):
    first_patterns=[]
    second_patterns=[]

    for i in range(0, len(path)):
        first_patterns.append(path[i][0])

    for i in range(0, len(path)):
        second_patterns.append(path[i][1])

    prefiks=first_patterns[0]
    sufiks=second_patterns[0]

    for i in range(1,len(first_patterns)):
        prefiks=prefiks+first_patterns[i][-1]

    for i in range(1,len(second_patterns)):
        sufiks=sufiks+second_patterns[i][-1]

    for i in range(k+d+1,len(prefiks)):
        if(prefiks[i]!=sufiks[i-k-d]):
            return "there is no string spelled by the gapped patterns"
    return prefiks+sufiks[len(sufiks)-k-d:]
        

def string_reconstruction(k,d,niz):
    D=debrujin(niz)
    path=eulerian_path(D)
    string=string_spelled_gapped_patterns(path,k,d)
    return string

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3j.txt","r") as f:
        k,d=map(int,f.readline().strip().split())
        niz=[line.strip().split("|") for line in f.readlines()]
    rezultat=string_reconstruction(k,d,niz)

    print(rezultat)

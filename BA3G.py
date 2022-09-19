def eulerian_cycle(D,pocetni_cvor):
    pocetni=pocetni_cvor
    trenutni=pocetni
    rezultat=[pocetni]

    while D:
        if trenutni in D:
            rezultat.append(D[trenutni][0])
            if len(D[trenutni])==1:
                del D[trenutni]
            else:
                del D[trenutni][0]
            trenutni=rezultat[-1]
        else:
            for i,j in enumerate(rezultat):
                if j in D:
                    ciklus_drugacije=rezultat[i:]+rezultat[1:i+1]
                    rezultat=ciklus_drugacije
                    trenutni=j
                    break
    return rezultat

from collections import Counter

def dodatni(D):
    broj_ulaznih_bridova=Counter()
    broj_izlaznih_bridova=Counter()

    for cvor,izlazni in D.items():
        broj_izlaznih_bridova[cvor]=broj_izlaznih_bridova[cvor]+len(izlazni)
        for izlaz in izlazni:
            broj_ulaznih_bridova[izlaz]=broj_ulaznih_bridova[izlaz]+1

    pocetni_cvor=list(broj_izlaznih_bridova-broj_ulaznih_bridova)[0]
    zavrsni_cvor=list(broj_ulaznih_bridova-broj_izlaznih_bridova)[0]

    if zavrsni_cvor in D:
        D[zavrsni_cvor]=D[zavrsni_cvor]+[pocetni_cvor]
    else:
        D[zavrsni_cvor]=[pocetni_cvor]
    return pocetni_cvor,zavrsni_cvor,D

def eulerian_path(D):
    pocetni_cvor,zavrsni_cvor,D=dodatni(D)
    eulerian_path=eulerian_cycle(D,pocetni_cvor)[1:]

    for i in range(len(eulerian_path)):
        if(eulerian_path[i]==zavrsni_cvor and eulerian_path[i+1]==pocetni_cvor):
            return eulerian_path[i+1:]+eulerian_path[:i+1]

    return eulerian_path
    

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3g(1).txt","r") as f:
        graph=[line.strip().split(" -> ") for line in f.readlines()]

    D=dict()

    for i in range(0,len(graph)):
        D[graph[i][0]]=graph[i][1].split(",")

    rezultat=eulerian_path(D)

    print("->".join(rezultat))

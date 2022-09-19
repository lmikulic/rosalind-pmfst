def eulerian_cycle(D):
    pocetni=list(D.keys())[0]
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
            
if __name__=="__main__":
    with open("../Downloads/rosalind_ba3f.txt","r") as f:
        graph=[line.strip().split(" -> ")for line in f.readlines()]

    D=dict()
    for i in range(0, len(graph)):
        D[graph[i][0]]=graph[i][1].split(",")

    rezultat=eulerian_cycle(D)
    print("->".join(rezultat))

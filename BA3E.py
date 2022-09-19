def deBruijn(uzorci):
    niz1=[]

    duljina=len(uzorci)
    duljina_uzorka=len(uzorci[0])

    for i in range(0, duljina):
        uzorak=uzorci[i]
        niz1.append(uzorak[0:(duljina_uzorka-1)]+" -> "+uzorak[1:(duljina_uzorka)])

    dodatni_pozicija=[]

    for j in range(0, duljina-1):
        for l in range(j+1, duljina):
            if(((niz1[j])[0:(duljina_uzorka-1)])==((niz1[l])[0:(duljina_uzorka-1)])):
                (niz1[j])=(niz1[j])+","+(niz1[l])[(duljina_uzorka+3):(2*(duljina_uzorka-1)+4)]
                dodatni_pozicija.append(l)

    dodatni_pozicija2=[]

    for element in dodatni_pozicija:
        if(dodatni_pozicija2.count(element)==0):
            dodatni_pozicija2.append(element)

    dodatni_pozicija2.sort()

    dulj=len(dodatni_pozicija2)
    while(dulj>0):
        niz1.pop(dodatni_pozicija2[dulj-1])
        dulj=dulj-1

    return niz1

if __name__=="__main__":
    with open("../Downloads/rosalind_ba3e.txt", "r") as f:
        uzorci=[line.strip() for line in f.readlines()]
    rezultat=deBruijn(uzorci)
    for element in rezultat:
        print(element)

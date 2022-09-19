Peptide=input("Peptide: ")

aminoacid=["G","A","S","P","V", "T", "C", "I", "L", "N", "D", "K", "Q", "E", "M", "H", "F", "R", "Y", "W"]

mass=[57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]

def izracunajMasu(subpeptide):
    rezultat=0

    for k in range(0, len(subpeptide)):
        for l in range(0, 20):
            if(aminoacid[l]==subpeptide[k]):
                rezultat=rezultat+mass[l]
                break
    return rezultat

lista=[]

prosireni=Peptide+Peptide

for i in range(0, len(Peptide)):
    for j in range(1, len(Peptide)):
        lista.append(prosireni[i:i+j])

lista_masa=[]
lista_masa.append(0)

for el in lista:
    lista_masa.append(izracunajMasu(el))

lista_masa.append(izracunajMasu(Peptide))
lista_masa.sort()

for masa in lista_masa:
    print(masa, end=" ")

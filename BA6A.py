def greedy_sorting(str_permutation):
    helper = [int(x) for x in str_permutation[1:-1].split()]

    S = []

    for i in range(0, len(helper)):
        if helper[i] == i + 1:
            continue

        idx = i
        while True:
            if helper[idx] == i + 1 or helper[idx] == -1 * (i + 1):
                break
            idx += 1

        mid = [-1 * x for x in helper[i : (idx + 1)]][::-1]
        helper = helper[0:i] + mid + helper[(idx + 1) :]
        S.append(helper.copy())

        if helper[i] < 0:
            helper[i] = abs(helper[i])
            S.append(helper.copy())

    return S

def drugacijiZapis(permutations):
    strings = []
    for perm in permutations:
        pomocni=[]
        for p in perm:
            if(p>=0):
                pomocni.append("+"+str(p))
            else:
                pomocni.append(str(p))
        pomocni2="("
        for el in pomocni:
            pomocni2=pomocni2+el+" "
        pomocni2=pomocni2[:-1]+")"
        strings.append(pomocni2)
    return strings

if __name__=="__main__":
    with open("../Downloads/rosalind_ba6a.txt", "r") as f:
        permutacija=[line.strip() for line in f.readlines()]
    rezultat=greedy_sorting(permutacija[0])
    strings=drugacijiZapis(rezultat)
    for element in strings:
        print(element)

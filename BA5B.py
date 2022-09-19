def manhattanTourist(n,m,down,right):
    s=[]
    for i in range(0,n+1):
        s.append((m+1)*[0])

    for j in range(1,n+1):
        s[j][0]=s[j-1][0]+down[j-1][0]

    for k in range(1,m+1):
        s[0][k]=s[0][k-1]+right[0][k-1]

    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j]=max(s[i-1][j]+down[i-1][j],s[i][j-1]+right[i][j-1])

    return s[n][m]

if __name__=="__main__":
    with open("../Downloads/rosalind_ba5b.txt", "r") as f:
        n,m=map(int, f.readline().strip().split())
        sve=[line.strip() for line in f.readlines()]
        br=0
        down=[]
        right=[]
        while(sve[br]!="-"):
            down.append(sve[br])
            br=br+1
        br=br+1
        while(br!=(n+n+2)):
            right.append(sve[br])
            br=br+1
        for i in range(0,n):
            element1=down[i]
            element1=element1.split(" ")
            down[i]=element1
        for j in range(0,n+1):
            element2=right[j]
            element2=element2.split(" ")
            right[j]=element2
        for i in range(0,n):
            for j in range(0,m+1):
                down[i][j]=int(down[i][j])
        for i in range(0,n+1):
            for j in range(0,m):
                right[i][j]=int(right[i][j])
    rezultat=manhattanTourist(n,m,down,right)
    print(rezultat)

def DPChange(money, coins):
    minnumcoins=(money+1)*[0]

    for i in range(1,money+1):
        minnumcoins[i]=i+1
        for c in coins:
            if(i>=c):
                if((minnumcoins[i-c]+1)<minnumcoins[i]):
                    minnumcoins[i]=minnumcoins[i-c]+1
    return minnumcoins[money]

Money=input("Money: ")
Money=int(Money)

Coins=input("Coins: ")
Coins=Coins.split(",")

for j in range(0, len(Coins)):
    Coins[j]=int(Coins[j])

print(DPChange(Money,Coins))

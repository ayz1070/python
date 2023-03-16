coins = [500,100,50,10]
money = list()

def exchange(n):
    for coin in coins:
        money.append(n//coin)
        n=n%coin

def get_integer():
    return int(input())


n = get_integer()
exchange(n)

i=0
for coin in coins:
    print(coin,"원 동전의 개수: ",money[i])
    i+=1



    
        
    
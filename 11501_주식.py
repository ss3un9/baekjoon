T=int(input())

for test_case in range(T):
    
    n=int(input())
    
    price=list(map(int,input().split()))
    max_price=0
    result=0
    for i in range(len(price)-1,-1,-1):
        if price[i]>max_price:
            max_price=price[i]
        else:
            result+=(max_price-price[i])
    print(result)
        
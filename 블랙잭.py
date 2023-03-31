import itertools

N,M=map(int,input().split())

card_list=list(map(int,input().split()))
max_sum=0
card_lst=itertools.combinations(card_list, 3)

for card in card_lst:
    if max_sum<sum(card)<=M:
        max_sum=sum(card)
        
print(max_sum)
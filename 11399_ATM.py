N=int(input())

P_lst=list(map(int,input().split()))

P_lst.sort()

result=[]
result.append(P_lst[0])
for i in range(1,len(P_lst)):
    p=(result[i-1]+P_lst[i])
    result.append(p)
print(sum(result))


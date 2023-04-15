import sys
intput=sys.stdin.readline
n=int(input())
plus,minus=[],[]
tmp=[]

for i in range(n):
    a=int(input())
    if a>1:
        plus.append(a)
    elif a<=0:
        minus.append(a)
    else:
        tmp.append(a)
plus.sort(reverse=True)
minus.sort()
#print(plus)
#print(minus)   
answer=0 
len_plus , len_minus=len(plus),len(minus)
result=[]
for i in range(0,len(plus),2):
    if i+1<len(plus):
        result.append(plus[i]*plus[i+1])
    else:
        result.append(plus[i])

for i in range(0,len(minus),2):
    if i+1<len(minus):
        result.append(minus[i]*minus[i+1])
    else:
        result.append(minus[i])
#print(tmp)
answer=sum(result)+sum(tmp)

print(answer)

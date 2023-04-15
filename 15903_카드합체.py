import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split())

num=list(map(int,input().split()))

#num.sort()
heapq.heapify(num)
for i in range(m):
    x=heapq.heappop(num)
    y=heapq.heappop(num)
    res=x+y
    heapq.heappush(num,res)
    heapq.heappush(num,res)
print(sum(num))




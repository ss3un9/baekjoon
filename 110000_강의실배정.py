import sys
import heapq
input=sys.stdin.readline

N=int(input())
time=[]
for _ in range(N):
    s,e=map(int,input().split())
    time.append([s,e])
    
time.sort()

heap=[]

heapq.heappush(heap,time[0][1])

for i in range(1,N):
    if time[i][0]>=heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1])
    
print(len(heap))

# heapq : : heappop 할 때마다 최소값을 찾아서 pop 하고 그 다음 최소값을 [0] 위치에 갖다놓는다
# 따라서, heappop 을 k 번 호출하면서 최소값을 갱신하면 최종 최소값이 k 번째 최소값이 된다.

        
    


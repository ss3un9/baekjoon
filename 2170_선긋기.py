import sys
import heapq
input=sys.stdin.readline

N=int(input())
line=[]

for i in range(N):
    s,e=map(int,input().split())
    line.append([s,e])
line.sort()
start=[line[0][0]]
heap=[line[0][1]]
heapq.heapify(heap)
heapq.heapify(start)
result=0
for i in range(1,N):
    if line[i][0]>heap[0]:
        result+=heap[0]-start[0]
        #heapq.heappop(heap)
        heapq.heappushpop(heap,line[i][1])
        #heapq.heappop(start)
        heapq.heappushpop(start,line[i][0])

    elif line[i][1]>heap[0] and line[i][0]>start[0]:         
        #heapq.heappop(heap)
        heapq.heappushpop(heap,line[i][1])   

result+=heap[0]-start[0]
print(result)
# for i in range(1,N):
#     if line[i][0] >heap[0]:
#         heapq.heappush(heap,line[i][1])
#         start.append(line[i][0])
#     heapq.heappop(heap)
#     heapq.heappush(heap,line[i][1])
# print(start)
# print(heap)
# res=[x-y for x,y in zip(heap, start)]
# print(sum(res))
    
    
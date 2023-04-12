import sys
input = sys.stdin.readline
N=int(input())
start_end=[]

for i in range(N):
    flowers=list(map(int,input().split()))
    time=[(flowers[0]*100)+flowers[1],(flowers[2]*100)+flowers[3]]
    start_end.append(time)
start_end.sort()



#start_end[x][0] 시작 
#satrt_end[x][1] 끝
last_start = 101
last_end = 301
temp_start = temp_end = count = 0
while last_end <= 1130 and count < 10000:  
    for i in range(N): 
        if start_end[i][0] <= last_end and \
            start_end[i][1] > last_end and \
            start_end[i][0] >= temp_start and \
            start_end[i][1] >= temp_end: 
                temp_start = start_end[i][0] 
                temp_end = start_end[i][1]  
    last_start = temp_start
    last_end = temp_end
    count += 1

if count == 10000: 
    print(0)
else:
    print(count)
    

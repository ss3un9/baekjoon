N = int(input())
time = []
for i in range(N):
    s,e = map(int, input().split())
    time.append([s,e])
#이렇게도 가능 
#time.sort(key = lambda a: (a[1], a[0]))
time = sorted(time, key=lambda a: a[0]) 
time = sorted(time, key=lambda a: a[1]) 
last = 0 
conut = 0 
for start, end in time:
    if start >= last: 
        conut += 1
        last = end
print(conut)
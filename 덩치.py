n = int(input())
lst=[]

for i in range(n):
    w, h = map(int, input().split())
    lst.append((w, h))

for i in lst:
    cnt = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')
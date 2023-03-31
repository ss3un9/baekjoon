import sys

n=int(input())
arr=[]
for i in range(n):
    str=input()
    arr.append(list(str))

cnt=n

for i in range(len(arr)):
    lst=[]
    test=arr[i][0]
    
    for j in range(0,len(arr[i])-1):

        
        if arr[i][j] !=arr[i][j+1]:
            lst.append(arr[i][j])
        
        if arr[i][j+1] in lst:
            
            cnt-=1
            break
            

print(cnt)

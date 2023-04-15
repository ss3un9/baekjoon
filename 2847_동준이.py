import sys
input=sys.stdin.readline

N=int(input())
score=[]
for _ in range(N):
    a=int(input())
    score.append(a)
answer=0
for i in range(N-1,0,-1):
    if score[i-1]>=score[i]:
        answer+=score[i-1]-score[i]+1
        score[i-1]=(score[i]-1)

print(answer)
        
    
    
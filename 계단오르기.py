import sys

N = int(input())
score=[int(input()) for _ in range(N)]

dp=[0]*N

if N<3:
    print(sum(score))
    exit()

dp[0]=score[0]
dp[1]=score[0]+score[1]

for i in range(2,N):
    dp[i]=max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])

print(dp[-1])    
'''
전전전칸+전칸+N
전전칸+N'''
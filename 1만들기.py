import sys

'''n=1 ->0
n=2 ->1
n=3 ->1
n=4 ->2
n=5 ->3
n=6 ->2
n=7 ->3
n=8 ->3
n=9 ->2
n=10 ->3


n이 %3==0 일때 /3
n이 %2==0 일때 /2
아닐땐 -1 
'''
N=int(input())
dp=[0]*(N+1)

for i in range(2,N+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

print(dp[N])
        
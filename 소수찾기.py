n=int(input())
num_list=list(map(int,input().split()))
cnt=0

def is_prime_num(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
if 1 in num_list:
    num_list.remove(1)

for i in num_list:
    if is_prime_num(i)==True:
        cnt+=1
print(cnt)
    
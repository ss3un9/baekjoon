import sys
input=sys.stdin.readline

num=str(input())

lst1=num.split('1')
lst0=num.split('0')

result1=0
result0=0

for i in lst1:
    if "0" in i:
        result1 += 1

for i in lst0:
    if "1" in i:
        result0 += 1

print(min(result1, result0))

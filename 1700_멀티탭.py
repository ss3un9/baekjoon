import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())

seq=list(map(int,input().split()))
plug_in=[]



cnt=0
for i,item in enumerate(seq):
    if item in plug_in:
        continue
    if len(plug_in)<N:
        plug_in.append(item)
    else:
        val=0
        idx=0
        cnt+=1
        temp=seq[i:]
        for x in plug_in:
            if x in temp:
                target=temp.index(x)
                if idx<=target:
                    idx=target
                    val=x
            else:
                val=x
                break
        plug_in[plug_in.index(val)]=item
print(cnt)
        
        
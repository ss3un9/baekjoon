def binary_search(lst,target,left,right):
    left, right = 0, len(lst) - 1
    while left <= right:
        middle_idx = (left + right) // 2
        middle = lst[middle_idx]
        if target == middle:
            return 1
        elif middle > target:
            right = middle_idx - 1
        else:
            left = middle_idx + 1
    return 0

N=int(input())

N_list=list(map(int,input().split()))

M=int(input())

M_list=list(map(int,input().split()))

N_list.sort()

for i in M_list:
    result=binary_search(N_list, i, 0, len(N_list)-1)
    print(result)
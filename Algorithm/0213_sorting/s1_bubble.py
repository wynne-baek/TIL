import sys
sys.stdin = open('input.txt')

T = int(input())
arr = []
for _ in range(T):
    num = int(input())
    arr.append(num)
#print(arr) [5, 2, 3, 4, 1]

# 버블 정렬
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            continue
        else:
            continue
print(arr) # [1, 2, 3, 4, 5]

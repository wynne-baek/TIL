import sys
sys.stdin = open('input.txt')

T = int(input())
arr = []
for _ in range(T):
    num = int(input())
    arr.append(num)
#print(arr) [5, 2, 3, 4, 1]

# 카운트 정렬
count = [0] * (max(arr)+1)
for i in arr:
    count[i] += 1
#print(count) [0, 1, 1, 1, 1, 1]

for j in range(1, len(count)):
    count[j] += count[j-1]
#print(count) [0, 1, 2, 3, 4, 5]

result = [0] * len(arr)
for n in range(len(arr)-1, -1, -1):
    result[count[arr[n]]-1] = arr[n]
    count[arr[n]] -= 1
print(result) #[1, 2, 3, 4, 5]

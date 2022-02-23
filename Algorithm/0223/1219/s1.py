import sys
sys.stdin = open('input.txt')

def dfs(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in arr[v]:
                if not visited[w]:
                    stack.append(w)

for _ in range(10):
    T, road = map(int, input().split())
    course = list(map(int, input().split()))
    arr = [[] for _ in range(100)]
    #방향 있음!!
    for i in range(road):
        arr[course[i*2]].append(course[i*2+1])
    # print(arr1)
    # print(arr2)
    visited = [0] * 100
    dfs(0)
    result = 1 if visited[99] else 0
    print(f'#{T} {result}')


import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    # 경로를 저장할 스택
    stack = []
    # 방문 여부를 확인할 visited
    visited = [0] * (V+1)
    stack.append(start)
    #스택이 텅 빌때까지
    while stack:
        v = stack.pop()
        visited[v] = 1
        for w in range(V+1):
            # 아직 w 방문 전이면
            if not visited[w]:
                # 방문 가능한가? 가능하면
                if course[v][w]:
                    #stack에 w 추가
                    stack.append(w)
    return visited[end]

T = int(input())
for _ in range(1, T+1):
    V, E = map(int, input().split())
    #인접 리스트 만들기
    course = [[0] * (V+1) for _ in range(V+1)]
    for __ in range(E):
        start, end = map(int, input().split())
        course[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{_} {dfs(S, G)}')



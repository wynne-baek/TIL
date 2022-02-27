import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수
T = int(input())
# 수강생 수 N, 제출한 사람의 수 K
for _ in range(1, T+1):
    N, K = map(int, input().split())
    # 과제를 제출한 사람의 번호 K 개
    submit = list(map(int, input().split()))
    # 제출하지 않은 사람의 번호를 오름차순 출력
    result = []
    for i in range(1, N+1):
        if i in submit:
            continue
        else:
            result.append(i)
    print(f'#{_}', *result)
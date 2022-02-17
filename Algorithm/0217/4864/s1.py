import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    search = input()
    whole = input()
    # - : 시작점
    # 회문 없으면 무조건 0 출력
    result = 0
    for _ in range(len(whole) - len(search) + 1):
        for i in range(len(search)):
            if search[i] != whole[_ + i]:
                break
        # for else 구문 활용해보기 (현영님 짱!)
        else:
            result = 1

    print(f'#{tc} {result}')


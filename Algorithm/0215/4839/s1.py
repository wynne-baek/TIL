import sys
sys.stdin = open('input.txt')

#재귀함수 활용
def CenterCnt(l, r, p, cnt):  # 좌 , 우, 찾아야 하는 페이지, count
    c = int((r + l) / 2)
    #탈출 조건 설정
    if c == p:
        return cnt
    #좌 우를 c 값으로 대체
    else:
        if c > p:
            return CenterCnt(l, c, p, cnt+1)
        else:
            return CenterCnt(c, r, p, cnt+1)
#테스트케이스 갯수
T = int(input())
for _ in range(T):
    # P:전체 쪽 수 Pa:a가 찾아야 하는 페이지 Pb: b가 찾아야 하는 페이지
    P, Pa, Pb = map(int,input().split())
    #위너 기본값 초기화
    winner = 0
    #함수 돌리기
    cnt_a = CenterCnt(1, P, Pa, 0)
    cnt_b = CenterCnt(1, P, Pb, 0)
    # 누가 이겼지?
    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_a > cnt_b:
        winner = 'B'
    print(f'#{_+1} {winner}')


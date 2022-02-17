import sys
sys.stdin = open('input.txt')

TC = int(input())
for _ in range(1, TC+1):
    A, B = input().split()
    #print(A, B)
    # A에서 B길이만큼 잘라서 비교
    i = 0
    cnt = 0
    while i < len(A):
        if B[0] == A[i]:
            if B == A[i:i + len(B)]:
                cnt += 1
                i += len(B)
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    print(f'#{_} {cnt}')
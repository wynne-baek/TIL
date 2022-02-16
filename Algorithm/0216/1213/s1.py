import sys
sys.stdin = open('input.txt')

for _ in range(10):
    TC = int(input())
    search = input()
    S = input()
    len_sear = len(search)
    #print(len(S))
    cnt = 0
    for i in range(len(S) - len_sear + 1):
        if search == S[i:i + len_sear]:
            cnt += 1
    print(f'#{TC} {cnt}')

import sys
sys.stdin = open('input.txt')

def pallindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i - 1]:
            return False
    return True

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    case = []
    for row in range(N):
        case.append(str(input()))
    #print(case)
    # row
    for word in case:
        #단어
        for i in range(N - M + 1):
            if pallindrome(word[i:i+M]) == True:
                print(f'#{_+1}', word[i:i+M])
    # column - 전치행렬 만들기
    case_2 = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            case_2[j][k] = case[k][j]
    #print(case_2)
    for col in case_2:
        for l in range(N - M + 1):
            if pallindrome(col[l:l+M]) == True:
                print(f'#{_+1}',''.join(col[l:l+M]))

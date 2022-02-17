import sys
sys.stdin = open('input.txt')

def pallindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i - 1]:
            return False
    return True

T = 10
for _ in range(1, 11):
    size = int(input())
    #가로
    arr = [list(input()) for i in range(8)]
    #세로(전치행렬)
    arr2 = [list(x) for x in zip(*arr)]
    #print(arr2)
    cnt = 0
    for lst in arr:
        for i in range(8 - size + 1):
            if pallindrome(lst[i:i+size]) == True:
                cnt += 1
    for lst2 in arr2:
        for i in range(8 - size + 1):
            if pallindrome(lst2[i:i+size]) == True:
                cnt += 1
    print(f'#{_} {cnt}')
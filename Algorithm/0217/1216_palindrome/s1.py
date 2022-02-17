import sys
sys.stdin = open('input.txt')

#회문 함수 작성
def pallindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i - 1]:
            return False
    return True

for _ in range(10):
    T = int(input())
    #리스트에 각 열 저장
    case_a = [list(input()) for i in range(100)]
    #전치행렬
    case_b = list(zip(*case_a))
    #최종결과에 1 저장 why? 1글자는 무조건 회문이니까
    result = 1
    #갯수 100개부터 거꾸로
    for length in range(100, 1, -1):
        if result >= length:
            break
        #횟수
        for k in range(100 - length + 1):
            if result == length:
                break
            for lst, lst2 in zip(case_a, case_b):
                if pallindrome(lst[k:k+length]) or pallindrome(lst2[k:k+length]):
                    result = length
                    break
    print(f'#{T} {result}')



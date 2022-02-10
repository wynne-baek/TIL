#N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
import sys
sys.stdin = open('input.txt')

T = int(input())
#print(T)
for _ in range(T):
    tc = int(input())
    tc_list = list(map(int, input().split()))
    #print(tc)
    result = max(tc_list) - min(tc_list)
    print(f'#{_+1}',result)


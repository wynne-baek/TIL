import sys
sys.stdin = open('input.txt')

N = int(input())
a = b = c = 0
if ((N % 101) % 11) % 2 == 0:
    a = N // 101
    b = (N % 101) // 11
    c = ((N % 101) % 11) // 2
elif ((N % 101) % 11) % 2 != 0:
    a = (N // 101) - 1
    b = (((N % 101) + 101) // 11) - 1
    c = (N - ((a * 101) + (b * 11))) // 2
print(a*100 + b* 10 + c)
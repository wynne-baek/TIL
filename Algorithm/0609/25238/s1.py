import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
bangmoo = a - (a*b/100)
if bangmoo >= 100:
    print(0)
else:
    print(1)
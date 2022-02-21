T = int(input())
change = 1000 - T
# 500, 100, 50, 10, 5, 1
a = change // 500
b = (change % 500) // 100
c = ((change % 500) % 100) // 50
d = (((change % 500) % 100) % 50) // 10
e = ((((change % 500) % 100) % 50) % 10) // 5
f = ((((change % 500) % 100) % 50) % 10) % 5
answer = a + b + c + d + e + f
print(answer)
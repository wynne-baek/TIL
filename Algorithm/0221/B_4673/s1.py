# d(n) = n + (n//10) + (n%10)
nums = set(range(1, 10001))
remove = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove.add(i)
answer = nums - remove
for num in sorted(answer) :
    print(num)
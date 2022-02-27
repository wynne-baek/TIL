nums = set(range(1, 10001))
# 빈 세트 생성
remove = set()
# i 를 생성자로 두는 숫자를 remove에 추가
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove.add(i)
# nums 세트에서 remove 세트를 빼면 정답인데,
answer = nums - remove
# 정렬된 상태로 프린트해주어야 함!
for num in sorted(answer) :
    print(num)
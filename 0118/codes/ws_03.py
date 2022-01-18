number = int(input())

# for문으로 number 까지 반복
for i in range(1, number+1):
    for pyramid in range(1, i+1):
        print(pyramid, end = ' ')
    print()
 
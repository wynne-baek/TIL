scores = [80, 89, 99, 83]

sum = 0

#for로 모든 요소 더해서 sum 만들기
for score in scores:
    sum = sum + score

#sum을 score의 갯수로 나누기
print(sum/len(scores))
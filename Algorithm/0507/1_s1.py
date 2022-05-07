def solution(survey, choices):
    answer = ''
    """
    카테고리 별로 딕셔너리를 만들어서 해당하는 키의 value에 값을 더해주고
    그 후에 값을 비교해서 유형을 정하면!
    """
    # 딕셔너리, 튜플로 각 카테고리별 점수와 선택별 점수 저장
    category = {
    'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0,
    'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0
    }
    score = (0, 3, 2, 1, 0, 1, 2, 3)
    # 반복문 돌면서 체크
    for i in range(len(survey)):
        if choices[i] < 4:
            category[survey[i][0]] += score[choices[i]]
        elif choices[i] > 4:
            category[survey[i][1]] += score[choices[i]]
    #print(category)
    if category['R'] >= category['T']:
        answer += 'R'
    else:
        answer += 'T'
    if category['C'] >= category['F']:
        answer += 'C'
    else:
        answer += 'F'
    if category['J'] >= category['M']:
        answer += 'J'
    else:
        answer += 'M'
    if category['A'] >= category['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
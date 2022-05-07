from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    """
    i) 두 큐의 원소 중 가장 큰 값이 두 큐 전체 원소의 합/2 보다 크면 -1 리턴
    ii) 두 큐의 원소 중 가장 큰 값이 두 큐 전체 원소의 합 /2 이면 얘 빼고 나머지는 다 한 쪽에 몰아야 함
    iii) 나머지 경우는, 원소의 합을 비교해서 큰 곳에서 작은 곳으로 보내주기
    """
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    all_sum = sum_1 + sum_2
    max_1 = max(queue1)
    max_2 = max(queue2)
    # 0) 만약 시행하기 전 이미 합이 같다면 아래부분 수행할 필요 없이 리턴
    # 예) [5], [5], 원소가 같고 길이가 모두 1인 경우에는 pop insert를 수행하지 않아도 됨
    if sum_1 == sum_2:
        answer = 0
        return answer
    # i)
    if (max_1 > all_sum/2) or (max_2 > all_sum/2):
        answer = -1
        return answer
    # ii)두 큐의 길이가 모두 2 이상일 때, max 값이 전체 큐의 합의 반과 같을 경우 수행!
    if max_1 == all_sum/2:
        answer = len(queue2) + (queue1.index(max_1))* 2 + 1
        return answer
    if max_2 == all_sum/2:
        answer = len(queue1) + (queue2.index(max_2))* 2 + 1
        return answer
    # iii)
    flag = True
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    our_len = len(queue1)+len(queue2)
    while flag:
        if answer > our_len:
            answer = -1
            return answer
        if sum_1 == sum_2:
            return answer
        elif sum_1 > sum_2:
            x = queue1.popleft()
            queue2.append(x)
            sum_1 -= x
            sum_2 += x
            answer += 1
        elif sum_1 < sum_2:
            x = queue2.popleft()
            queue1.append(x)
            sum_1 += x
            sum_2 -= x
            answer += 1
    return answer


"""6513. 15
2724.  15"""
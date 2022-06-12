def solution(periods, payments, estimates):
    answer = [0, 0]
    """
    vip 여부 먼저 판독
    - 24개월 이상 and 납부내역 90만원 이상
    - 60개월 이상 and 60만원 이상
    1) vip가 되는 고객
    - vip가 아니면서
    - 다음달 납부 금액이 기준 충족
    2) vip가 아니게 되는 고객
    - vip면서
    - 기준 미충족
    """
    people = len(periods)
    # 금액 확인
    sum_of_payments = []
    sum_of_estimate = []
    for i in range(people):
        temp = sum(payments[i])
        sum_of_payments.append(temp)
        temp = temp - payments[i][0] + estimates[i]
        sum_of_estimate.append(temp)
    # print(sum_of_payments)
    # print(sum_of_estimate)
    VIP = []
    VIP_estimate = []
    for i in range(people):
        if (periods[i] >= 24 and sum_of_payments[i] >= 900000) or (periods[i] >= 60 and sum_of_payments[i] >= 600000):
            VIP.append(True)
        else:
            VIP.append(False)
        if (periods[i] + 1 >= 24 and sum_of_estimate[i] >= 900000) or (periods[i] + 1 >= 60 and sum_of_estimate[i] >= 600000):
            VIP_estimate.append(True)
        else:
            VIP_estimate.append(False)
    # print(VIP)
    # print(VIP_estimate)

    for i in range(people):
        if not VIP[i] and VIP_estimate[i]:
            answer[0] += 1
        elif VIP[i] and not VIP_estimate[i]:
            answer[1] += 1

    return answer
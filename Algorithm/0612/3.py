def solution(n, plans, clients):
    people = len(clients)
    answer = [0] * people
    """
    plans는 m개,부가서비스 n개
    문자열로 제공데이터, 제공하는 부가서비스
    고객도 문자열로 원하는 데이터, 원하는 부가서비스
    가장 작은 요금제 번호
    """
    for j in range(people):
        a = list(map(int, clients[j].split()))
        data = a[0]
        services = list(a[1:])
        give_service = []
        for i in range(len(plans)):
            b = list(map(int, plans[i].split()))
            give_data = b[0]
            give_service += list(b[1:])
            # print(give_service)
            if data > give_data:
                continue

            for service in services:
                # print(service)
                # print(give_service)
                if service not in give_service:
                    break
            else:
                answer[j] = i + 1
                break

    return answer
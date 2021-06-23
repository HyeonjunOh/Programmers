def solution(record):
    d = {}
    answer = []
    for i in record:
        p = i.split(" ")
        if p[0] == "Enter":
            d[p[1]] = p[2]
            answer.append([p[1], "님이 들어왔습니다."])
        elif p[0] == "Change":
            d[p[1]] = p[2]
        else:
            answer.append([p[1], "님이 나갔습니다."])
    return [d[i[0]]+i[1] for i in answer]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
def solution(dartResult):
    answer = []
    tmp = ""
    for i in dartResult:
        k = len(answer)
        if i.isdigit():
            tmp += i
        elif i.isalpha():
            answer.append(int(tmp)**int("SDT".index(i)+1))
            tmp = ""
        elif i == "*":
            if k == 1:
                answer[0] *= 2
            else:
                answer[k-1] *= 2
                answer[k-2] *= 2
        else:
            answer[k-1] *= -1
    return sum(answer)

print(solution("1S*2T*3S"))
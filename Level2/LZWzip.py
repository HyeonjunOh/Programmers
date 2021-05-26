def solution(msg):
    answer = []
    d = {chr(i+65): i+1 for i in range(26)}
    i = 0
    w = msg[0]
    while i+1 <= len(msg):
        try:
            c = msg[i+1]
        except:
            c = ""
        if w+c in d:
            if i == len(msg)-1:
                answer.append(d[w+c])
                return answer
            else:
                w += c
                i += 1
        else:
            d[w+c] = len(d)+1
            answer.append(d[w])
            w = c
            i += 1
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# print(ord("Z"))#65-90
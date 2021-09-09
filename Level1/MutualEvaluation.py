def solution(scores):
    answer = ''
    d = {9: "A", 8: "B", 7: "C", 6: "D", 5: "D"}
    for idx, score in enumerate(zip(*scores)):
        if score[idx] in [min(score), max(score)] and score.count(score[idx]) == 1:
            s = (sum(score) - score[idx])/(len(score)-1)
        else:
            s = sum(score)/len(score)
        t = int(s*0.1)
        if t in d:
            answer += d[t]
        else:
            answer += "F"
    return answer




print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
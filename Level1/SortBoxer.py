def solution(weights, head2head):
    answer = []
    for i in range(len(weights)):
        win, lose, winh = 0, 0, 0
        tmp = [i+1, weights[i], 0, 0]
        for w, h in zip(weights, head2head[i]):
            if h == "W":
                win += 1
                if weights[i] < w:
                    winh += 1
            elif h == "L":
                lose += 1
        answer.append([i+1, weights[i], win/(win+lose) if win+lose != 0 else 0, winh])
    return [i[0] for i in sorted(answer, key= lambda x: (-x[2], -x[3], -x[1], x[0]))]


print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
def solution(line):
    result = []
    answer = set()
    for idx, abe in enumerate(line):
        a, b, e = abe
        for cdf in line[idx+1:]:
            c, d, f = cdf
            try:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if int(x) == x and int(y) == y:
                    answer.add((int(x), int(y)))
            except:
                continue
    r = [[min(i), max(i)] for i in zip(*answer)]
    for j in range(r[1][1], r[1][0]-1, -1):
        tmp = ""
        for i in range(r[0][0], r[0][1]+1):
            if (i,j) in answer:
                tmp += "*"
            else:
                tmp += "."
        result.append(tmp)
    return result


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
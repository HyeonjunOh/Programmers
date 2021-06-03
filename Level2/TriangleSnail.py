def solution(n):
    answer = [[0]*(i+1) for i in range(n)]
    idx1, idx2 = -1, 0
    num, cnt = 0, n
    while cnt != 0:
        for i in range(num, num+cnt):
            k = [[1, 0], [0, 1], [-1, -1]][(n-cnt)%3]
            idx1 += k[0]
            idx2 += k[1]
            answer[idx1][idx2] = i+1
        num += cnt
        cnt -= 1
    return sum(answer, [])

print(solution(6))
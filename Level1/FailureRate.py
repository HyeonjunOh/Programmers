def solution(N, stages):
    stop = {}
    cleared = {i: 0 for i in range(1, N+2)}
    for i in range(1, N+2):
        a = stages.count(i)
        stop[i] = a
        for j in range(1, i):
            cleared[j] += a
    for i in range(N):
        try:
            stop[i+1] = stop[i+1]/(stop[i+1]+cleared[i+1])
        except:
            stop[i+1] = 0
    stop.pop(N+1)
    return [i[0] for i in sorted(stop.items(), key=lambda x: (-x[1], x[0]))]


print(solution(10, [2, 1, 2, 6, 2, 4, 3, 3]))

# i:count
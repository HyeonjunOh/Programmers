def solution(n):
    p = [0, 0] + [1]*(n-1)
    i = 2
    while i*i <= n:
        for j in range(i*i, n+1, i):
            p[j] = 0
        i += 1
    return sum(p)


print(solution(10))
def solution(n, lost, reserve):
    s = [1 if (i in reserve and i in lost) else 2 if i in reserve else 0 if i in lost else 1 for i in range(1, n+1)]
    for i in range(n):
        if i != 0 and s[i] == 2 and s[i-1] == 0:
            s[i] -= 1
            s[i-1] += 1
        elif i != n-1 and s[i] == 2 and s[i+1] == 0:
            s[i] -= 1
            s[i+1] += 1
    return n - s.count(0)


print(solution(30, [2, 4], [1, 3, 5]))
print(solution(30, [2, 4], [3]))
print(solution(30, [3], [1, 5]))
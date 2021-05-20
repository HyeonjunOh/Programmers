def toBaseN(b, n):
    if n == 0: return "0"
    answer = ""
    base = "0123456789ABCDEF"
    while n != 0:
        n, t = n//b, n%b
        answer += base[t]
    return answer

def solution(n, t, m, p):
    answer = ""
    i, cnt = 0, 0
    num = ""
    while len(answer) != t:
        if num == "":
            num = toBaseN(n, i)
            i += 1
        if cnt%m == p-1:
            answer += num[-1]
        num = num[:-1]
        cnt += 1
    return answer

print(solution(16, 16, 2, 1))
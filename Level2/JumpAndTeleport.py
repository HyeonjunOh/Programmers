def solution(n):
    ans = 0
    while n > 2:
        n, t = divmod(n, 2)
        ans += t
    return ans+1

print(solution(5000))
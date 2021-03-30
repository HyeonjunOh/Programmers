def solution(n):
    return(int("".join(sorted(str(n))[::-1])))

print(solution(118372))
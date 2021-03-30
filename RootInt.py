def solution(n):
    return int((n**.5+1)**2) if not (n**.5+1)**2%1 else -1

print(solution(121))
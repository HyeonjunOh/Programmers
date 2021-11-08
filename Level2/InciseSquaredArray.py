def solution(n, left, right):
    arr = [[j+1 if j>=i else i+1 for j in range(n)] for i in range(left//n, right//n + 1)]
    return sum(arr, [])[left%n:left%n+right-left+1]

print(solution(3, 2, 5))
print(solution(4, 6, 14))
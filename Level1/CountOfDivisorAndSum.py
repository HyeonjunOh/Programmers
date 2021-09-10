solution = lambda left, right: sum([-k if sum([1 for i in range(1, k+1) if k%i == 0])%2 == 1 else k for k in range(left, right + 1)])
print(solution(1, 1))
from itertools import permutations

def isprime(n):
    if n < 2: return False
    i = 2
    while i <= n**.5:
        if n%i == 0: return False
        else: i += 1
    return True

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in permutations(numbers, i+1):
            k = int(''.join(j))
            if isprime(k): answer.add(k)
    return len(answer)

print(solution("011"))
def solution(n):
    count = 0
    for i in range(2, n+1):
        if prime(i):
            count += 1
    return count

def prime(n):
    i = 2
    while i*i <= n:
        if not n%i: return False
        else: i += 1
    return True

print(solution(10))
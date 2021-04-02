import itertools
def solution(nums):
    return len([sum(i) for i in itertools.combinations(nums, 3) if prime(sum(i))])

def prime(n):
    if n==1: return False
    i = 2
    while i*i <= n:
        if not n%i: return False
        else: i += 1
    return True


print(solution([1,2,7,6,4]))
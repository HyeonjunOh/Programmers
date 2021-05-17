import sys
sys.setrecursionlimit(100000)

def f(a, n):
    if a>n: return 0
    t = []
    for i in range(a, n+1):
        t.append(i)
        s = sum(t)
        if s == n: return 1 + f(a+1, n)
        elif s > n: return 0 + f(a+1, n)
def solution(n):
    return f(1, n)
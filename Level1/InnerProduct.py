# def solution(a, b):
#     return sum([a[i]*b[i] for i in range(len(a))])

def solution(a, b):
    return sum(i*j for i, j in zip(a,b))

print(solution())
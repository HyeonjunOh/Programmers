def mul(a):
    result = 1
    for i in a:
        result *= i
    return result
def solution(clothes):
    d = {}
    for i in clothes:
        if i[1] not in d:
            d[i[1]] = 1
        else:
            d[i[1]] += 1
    tmp = [i+1 for i in d.values()]
    return mul(tmp)-1

# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
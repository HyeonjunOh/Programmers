def solution(arr):
    answer = []
    while sum(arr) != len(arr):
        for i in range(2, max(arr)+1):
            if any([j%i == 0 for j in arr]):
                answer.append(i)
                arr = list(map(lambda x: x//i if x%i == 0 else x, arr))
                break
    result = 1
    for i in answer:
        result *= i
    return result

print(solution([2, 6, 8, 14]))


# 2번째 플이
# from math import gcd
# def nlcm(num):
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)
#     return answer
# print(nlcm([2,6,8,14]))


# 3번째 풀이
# def gcd(a, b):
#     a, b = max(a, b), min(a, b)
#     while b:
#         a, b = b, a%b
#     return a
#
# def solution(arr):
#     result = arr[0]
#     for i in range(len(arr)-1):
#         result *= arr[i+1]//gcd(result, arr[i+1])
#     print(result)
#
# solution([2, 6, 8, 14])
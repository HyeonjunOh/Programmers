def transpose(m):
    t = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    for idx1, i in enumerate(m):
        for idx2, j in enumerate(i):
            t[idx2][idx1] = m[idx1][idx2]
    return t

def dotproduct(a, b):
    result = 0
    for i, j in zip(a, b):
        result += i*j
    return result

def solution(arr1, arr2):
    result = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
    arr2 = transpose(arr2)
    for idx1, i in enumerate(arr1):
        for idx2, j in enumerate(arr2):
            result[idx1][idx2] = dotproduct(i, j)
    return result


# 2번째 풀이
# def solution(arr1, arr2):
#     return [[sum(a*b for a, b in zip(j, i)) for i in zip(*arr2)] for j in arr1]

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
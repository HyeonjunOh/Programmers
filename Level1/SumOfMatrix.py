def solution(arr1, arr2):
    return [[i+j for i, j in zip(k, l)]for k, l in zip(arr1, arr2)]

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
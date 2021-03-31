def solution(n, arr1, arr2):
    answer = []
    arr1 = ['0'*(n-len(bin(i)[2:]))+bin(i)[2:]for i in arr1]
    arr2 = ['0' * (n - len(bin(i)[2:])) + bin(i)[2:] for i in arr2]
    a = [[" #"['1' in i+j] for i, j in zip(k, l)] for k, l in zip(arr1, arr2)]
    for i in a:
        answer.append("".join(i))
    return answer
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
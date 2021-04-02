def solution(arr, divisor):
    answer = sorted([i for i in arr if i%divisor == 0])
    return answer if answer else [-1]

print(solution([5, 9, 7, 10], 5))
def solution(arr):
    return arr[-1]
    # return [arr[i] for i in range(len(arr)) if arr[i] != arr[i-1] or i == 0]

print(solution([1,1,3,3,0,1,1]))
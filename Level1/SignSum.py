def solution(absolutes, signs):
    # answer = 0
    # for i, j in zip(absolutes, signs):
    #     answer += [-i, i][j]
    # return answer
    return sum([-i, i][j] for i, j in zip(absolutes, signs))

print(solution([4,7,12], [True, False, True]))
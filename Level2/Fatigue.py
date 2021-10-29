# def solution(k, dungeons):
#     answer = 0
#     dungeons = sorted(dungeons, key=lambda x: (x[0]-x[1], -x[1], x[0]))
#     print(dungeons)
#     while dungeons:
#         tmp = dungeons.pop()
#         if tmp[0] <= k:
#             k -= tmp[1]
#             answer += 1
#     return answer

from itertools import permutations
def solution(k, dungeons):
    answer = []
    for i in permutations(dungeons):
        cnt = 0
        tmp_k = k
        for j in i:
            if j[0] <= tmp_k:
                tmp_k -= j[1]
                cnt += 1
        answer.append(cnt)
    return max(answer)
print(solution(80, [[80,20],[50,40],[30,10]]))
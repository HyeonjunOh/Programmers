# def solution(people, limit):
#     answer = 0
#     people = sorted(people, reverse=True)
#     while people:
#         p = people.pop(0)
#         if people and p + people[-1] <= limit:
#             for idx, person in enumerate(people):
#                 if p + person <= limit:
#                     people.pop(idx)
#                     break
#         answer += 1
#     return answer

# def solution(people, limit):
#     people.sort()
#     half_limit = limit//2
#     answer = 0
#     while people and people[-1] > half_limit:
#         answer += 1
#         p = people.pop()
#         if people and p + people[0] <= limit:
#             people.pop(0)
#     answer += (len(people)+1)//2
#     return answer

from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    half_limit = limit//2
    answer = 0
    while people and people[-1] > half_limit:
        answer += 1
        p = people.pop()
        if people and p + people[0] <= limit:
            people.popleft()
    answer += (len(people)+1)//2
    return answer


print(solution([70, 50, 80, 50], 100))
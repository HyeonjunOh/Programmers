# def solution(number, k):
#     idx = 1
#     answer = [number[0]]
#     while k != 0:
#         if not answer:
#             answer.append(number[idx])
#             idx += 1
#         if number[idx] > answer[-1]:
#             answer.pop()
#             k -= 1
#         else:
#             answer.append(number[idx])
#             idx += 1
#     return "".join(answer) + number[idx:]

def solution(number, k):
    idx = 0
    answer = []
    while k != 0:
        if not answer or (idx < len(number) and number[idx] <= answer[-1]):
            answer.append(number[idx])
            idx += 1
        else:
            answer.pop()
            k -= 1
    return "".join(answer) + number[idx:]



print(solution("11", 1))

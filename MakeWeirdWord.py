# def solution(s):
#     s = s.upper()
#     answer = ''
#     c = 0
#     for i in s:
#         if i == " ":
#             c = -1
#             answer += i
#         elif c%2 == 1:
#             answer += i.lower()
#         elif c%2 == 0:
#             answer += i
#         c += 1
#     return answer
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
print(solution("try    hello world"))
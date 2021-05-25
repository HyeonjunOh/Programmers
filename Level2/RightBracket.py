# def solution(s):
#     stack = ""
#     for i in s:
#         if i == "(":
#             stack += i
#         else:
#             if not stack:
#                 return False
#             else:
#                 stack = stack[:-1]
#     if stack:
#         return False
#     else:
#         return True

def solution(s):
    cnt = 0
    for i in s:
        if i == "(": cnt += 1
        else:
            if cnt <= 0:
                return False
            else:
                cnt -= 1
    return cnt == 0
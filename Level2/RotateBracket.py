def f(s):
    p = []
    b = [["[", "(", "{"], ["]", ")", "}"]]
    for i in s:
        if i in b[0]:
            p.append(i)
        else:
            if not p or p.pop() != b[0][b[1].index(i)]:
                return False
    return p == []
def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[0]
        answer += f(s)
    return answer

print(solution("{}[]()"))
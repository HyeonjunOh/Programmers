def bal(a):
    return a.count('(') == a.count(')')

def correct(a):
    if bal(a) and sum([i for i, j in enumerate(a) if j == "("]) <= sum([i for i, j in enumerate(a) if j == ")"]):
        return True
    else:
        return False

def rev(a):
    b = ""
    for i in a:
        if i == "(":
            b += ")"
        else:
            b += "("
    return b

def solution(p):
    if not p:
        return ""
    u, v = "", p
    for i in range(len(p)//2):
        if bal(p[:(i+1)*2]):
            u, v = p[:(i+1)*2], p[(i+1)*2:]
            break
    if correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + rev(u[1:-1])

print(solution("()))((()"))
def solution(s):
    a, b = 0, 0
    while s != "1":
        s, c = bin(s.count("1"))[2:], s.count("0")
        a += 1
        b += c
    return [a, b]

print(solution("110010101001"))
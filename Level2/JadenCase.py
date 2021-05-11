def solution(s):
    answer = ''
    for i, j in enumerate(s.lower()):
        if j.isalpha() and (i == 0  or s[i-1] == " "):
            answer += j.upper()
        else:
            answer += j
    return answer

print(solution("3people unFollowed me"))

# a = "3people    unFollowed me"
# print(' '.join([i.capitalize() for i in a.split(" ")]))
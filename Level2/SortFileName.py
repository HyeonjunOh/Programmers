def f(s):
    result = [s]
    for i in range(len(s)):
        if s[i+1].isdigit():
            result.append(s[:i+1].lower())
            s = s[i+1:]
            break
    for i in range(len(s)):
        if s[i].isdigit() and i == len(s)-1:
            result.append(int(s))
            break
        elif s[i].isdigit() and not s[i+1].isdigit():
            result.append(int(s[:i+1]))
            break
    return result

def solution(files):
    answer = []
    for i in files:
        answer.append(f(i))
    answer = [i[0] for i in sorted(answer, key=lambda x: (x[1], x[2]))]
    return answer

print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
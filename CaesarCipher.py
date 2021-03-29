def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        elif i.islower():
            answer += chr((ord(i)+n-97)%26+97)
        else:
            answer += chr((ord(i)+n-65)%26+65)
    return answer

print(solution("AB", 1))
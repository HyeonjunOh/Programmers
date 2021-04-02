def solution(n):
    answer = ""
    while n!=0:
        n, d = divmod(n, 3)
        answer += str(d)
    return int(answer, 3)

print(solution(125))


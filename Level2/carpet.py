def solution(brown, yellow):
    i = 1
    while i*i <= yellow:
        if yellow % i == 0 and (i+2)*(yellow//i+2) == (brown+yellow):
            return [yellow//i + 2, i+2]
        i += 1

print(solution(8, 1))
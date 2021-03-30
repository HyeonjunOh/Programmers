def solution(numbers, hand):
    answer = ''
    l, r = 10, 12
    for i in numbers:
        if i in [1,4,7]:
            l = i
            answer += "L"
        elif i in [3,6,9]:
            r = i
            answer += "R"
        else:
            if i == 0:
                i = 11
            lton = distance(divmod(l-1, 3), divmod(i-1, 3))
            rton = distance(divmod(r-1, 3), divmod(i-1, 3))
            if lton == rton:
                if hand == "left": l = i
                else: r = i
                answer += hand[0].upper()
            elif lton < rton:
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
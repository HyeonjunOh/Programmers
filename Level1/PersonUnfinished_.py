def solution(participant, completion):
    p = sorted(participant)
    for i in completion:
        left, right = 0, len(p)-1
        while left<=right:
            mid = (left+right)//2
            if p[mid] == i:
                p.remove(i)
                break
            elif p[mid] < i:
                left = mid + 1
            else:
                right = mid - 1
        if left > right:
            return i
    return p[0]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

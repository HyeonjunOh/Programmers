import datetime
def solution(a, b):
    d = datetime.datetime(2016, a, b)
    return ["MON","TUE","WED","THU","FRI","SAT","SUN"][d.weekday()]

print(solution(5, 3))
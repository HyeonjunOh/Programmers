def solution(id_list, report, k):
    be_reported = {i: set() for i in id_list}
    reported = {i: set() for i in id_list}
    for i in report:
        a, b = i.split()
        be_reported[b].add(a)
        reported[a].add(b)
    return [sum([1 if len(be_reported[j]) >= k else 0 for j in list(i)]) for i in reported.values()]



print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
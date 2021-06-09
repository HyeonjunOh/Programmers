# def solution(info, query):
#     d = {"cpp": set(), "java": set(), "python": set(), "backend": set(), "frontend": set(),
#          "junior": set(), "senior": set(), "chicken": set(), "pizza": set(), "-": set()}
#     score = []
#     answer = []
#     for idx, s in enumerate(info):
#         for i in s.split(" "):
#             if i.isdigit():
#                 score.append(int(i))
#             else:
#                 d[i].add(idx)
#             d["-"].add(idx)
#     for s in query:
#         s = s.replace("and", "").split(" ")
#         answer.append(len([score[i] for i in d[s[0]] & d[s[2]] & d[s[4]] & d[s[6]] if score[i] >= int(s[7])]))
#     return answer

from itertools import product
def solution(info, query):
    answer = []
    d = {}
    for s in info:
        s = s.split(" ")
        ss = [["-"] + [i] for i in s[:-1]]
        for i in product(*ss):
            tmp = "".join(i)
            if tmp in d:
                d[tmp].append(int(s[-1]))
            else:
                d[tmp] = [int(s[-1])]
    for i in query:
        k = i.replace(" and ", "").split(" ")
        try:
            answer.append(len([j for j in d[k[0]] if j >= int(k[1])]))
        except:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# d = {"java": {0, 1, 2}, "cpp": {2, 3}, "python": {0, 2, 3}}
# d["java"].add(5)
# print(d)
# d["java"] &= d["cpp"]
# print(d)
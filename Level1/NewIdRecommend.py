import re

#
# def step1(id):
#     return id.lower()
#
# def step2(id):
#     return "".join(filter(lambda x: x not in "~!@#$%^&*()=+[{]}:?,<>/", id))
#
# def step3(id):
#     return re.sub('[.]+', ".", id)
#
# def step4(id):
#     id += " "
#     return id[id[0]==".":-(1+(id[-2]=="."))]
#
# def step5(id):
#     return id if id else "a"
#
# def step6(id):
#     return step4(id[:15]) if len(id)>15 else id
#
# def step7(id):
#     id += id[-1]*(3-len(id))
#     return id

# def solution(new_id):
#     return step7(step6(step5(step4(step3(step2(step1(new_id)))))))

def solution(new_id):
    id = new_id.lower()
    id = "".join(filter(lambda x: x not in "~!@#$%^&*()=+[{]}:?,<>/", id))
    id = re.sub('[.]+', ".", id)+" "
    id = id[id[0] == ".":-(1 + (id[-2] == "."))]
    id = id if id else "a"
    id = id[:15]+" " if len(id) > 15 else id+" "
    id = id[id[0] == ".":-(1 + (id[-2] == "."))]
    id += id[-1] * (3 - len(id))
    return id

print(solution("abcdefghijklmn.p"))
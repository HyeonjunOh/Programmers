from collections import Counter
# 내 풀이
def solution(participant, completion):
    participant = Counter(participant)
    for i in completion:
        if i in participant:
            participant[i] -= 1
    for k, v in participant.items():
        if v == 1:
            return k

# 다른 사람 풀이
# def solution(participant, completion):
#     return list((Counter(participant) - Counter(completion)).keys())[0]
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
def solution(n, words):
    dup = []
    for cnt, word in enumerate(words):
        if word in dup or (dup and word[0] != dup[-1][-1]):
            return [cnt%n+1, cnt//n+1]
        else:
            dup.append(word)
    return [0, 0]

# def solution2(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
from itertools import product
def solution(word):
    words = []
    for i in range(5):
        for j in product("AEIOU", repeat=i+1):
            words.append("".join(j))
    return sorted(words).index(word)+1
print(solution("AAAE"))
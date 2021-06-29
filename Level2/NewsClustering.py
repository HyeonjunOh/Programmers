from collections import Counter
def solution(str1, str2):
    mul_set1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    mul_set2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    hash1 = Counter(mul_set1)
    hash2 = Counter(mul_set2)
    inter = sum([min(hash1[i], hash2[i]) for i in hash1 if i in hash2])
    sym_diff = sum([i for i in (hash1+hash2).values()]) - inter
    try:
        return int(inter/sym_diff*65536)
    except:
        return 65536
print(solution("aabbbb", "AAAAab"))
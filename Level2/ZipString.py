def solution(s):
    answer = []
    for i in range(len(s)):
        spl = [s[j:j+i+1] for j in range(0, len(s), i+1)]
        st = ""
        pre, count = "", 0
        for idx, j in enumerate(spl):
            if pre != j:
                st += [str(count) + pre, pre][count < 2]
                pre = j
                count = 1
            else:
                count += 1
            if idx == len(spl)-1:
                st += [str(count) + pre, pre][count < 2]
        answer.append(len(st))
    return min(answer)

#
# a = ["aabbaccc",
# "ababcdcdababcdcd",
# "abcabcdede",
# "abcabcabcabcdededededede",
# "xababcdcdababcdcd"]
#
# for i in a:
#     print(solution(i))
print(solution("aabbaccc"))
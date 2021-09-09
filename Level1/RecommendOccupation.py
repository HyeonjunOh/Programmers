def solution(table, languages, preference):
    answer = []
    d = {i: j for i, j in zip(languages, preference)}
    for i in table:
        tmp = i.split()
        answer.append([tmp[0], (sum([(5-j)*d[tmp[j+1]] for j in range(5) if tmp[j+1] in d]))])
    return sorted(answer, key=lambda x: (-x[1], x[0]))[0][0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
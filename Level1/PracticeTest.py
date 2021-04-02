def solution(answers):
    k = len(answers)
    a = [1,2,3,4,5]*(k//5+1)
    b = [2,1,2,3,2,4,2,5]*(k//8+1)
    c = [3,3,1,1,2,2,4,4,5,5]*(k//10+1)
    for i in range(k):
        a[i] = a[i]==answers[i]
        b[i] = b[i]==answers[i]
        c[i] = c[i]==answers[i]
    d = [sum(a[:k]), sum(b[:k]), sum(c[:k])]
    answer = [i+1 for i, j in enumerate(d) if j == max(d)]
    return answer
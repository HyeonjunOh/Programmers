def solution(board, moves):
    answer = 0
    a = [[board[j][i] for j in range(len(board))] for i in range(len(board))]
    b = []
    for i in moves:
        for j, k in enumerate(a[i-1]):
            if k != 0:
                b.append(a[i-1].pop(j))
                break
    while True:
        tmp = b
        for i in range(len(b)-1):
            if b[i]==b[i+1]:
                b = b[:i] + b[i+2:]
                answer += 2
                break
        if tmp==b:
            break
    return answer
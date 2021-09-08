def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(word):
        s = s.replace(j, str(i))
    return int(s)
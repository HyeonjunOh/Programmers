import time
import random

def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        tmp = phone_book[idx]
        if tmp == phone_book[idx+1][:len(tmp)]:
            return False
    return True

# def solution(phone_book):
#     d = {i: 1 for i in phone_book}
#     for number in phone_book:
#         tmp = ""
#         for i in number:
#             tmp += i
#             if tmp in d and tmp != number:
#                 return False
#     return True

st = time.time()
print(solution([str(random.randint(1, 1000000)) for i in range(1000000)]))
ft = time.time()
print(ft - st)
# import re
# def solution(s):
#     pattern = re.compile(r'((.)\2)+')
#     for k in s:
#         if s.count(k)%2 == 1:
#             return 0
#     while True:
#         ss = re.sub(pattern, "", s)
#         if s != ss:
#             s = ss
#         else:
#             break
#     return int(s == "")
def solution(s):
    st = []
    for i in s:
        if not st or st[-1] != i:
            st.append(i)
        else:
            st.pop()
    return int(st == [])

print(solution("baabaa"))

# a = "baaaa"
# p = re.compile(r'((.)\2)+')
# print(re.search(p, a))
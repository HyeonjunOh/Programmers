def caltime(t):
    a = list(map(int, t.split(":")))
    return a[0]*60+a[1]
def splitinfo(infos):
    playtime = caltime(infos[1])-caltime(infos[0])
    sheet = []
    tmp = infos[3]
    while tmp:
        if "#" in tmp[:2]:
            sheet.append(tmp[:2])
            tmp = tmp[2:]
        else:
            sheet.append(tmp[:1])
            tmp = tmp[1:]
    a, b = divmod(playtime, len(sheet))
    sheet = sheet*a+sheet[:b]
    return [playtime, infos[2], "".join(sheet)]

def solution(m, musicinfos):
    infos = [splitinfo(info.split(",")) for info in musicinfos]
    infos = [[idx]+i for idx, i in enumerate(infos) if m in i[2].replace(m+"#", "-")]
    try:
        return sorted(infos, key=lambda x: (x[1], -x[0]))[-1][2]
    except:
        return '(None)'

# splitinfo("12:00,12:14,HELLO,CDEFGAB")
print(solution(	"CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))
print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))
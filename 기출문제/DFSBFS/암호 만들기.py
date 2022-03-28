L,C = map(int, input().split())

alpha = list(input().split())

alpha.sort()
candidate = []
answer = []
ja = 0
mo = 0
def dfs(index):
    global ja, mo
    if len(candidate) == L:
        if ja >=2 and mo >= 1:
            answer.append("".join(candidate))
    else:
        for i in range(index + 1,len(alpha)):
            candidate.append(alpha[i])
            mo_flag = False
            ja_flag = False
            if alpha[i] in ['a','e','i','o','u']:
                mo += 1
                mo_flag = True
            else:
                ja += 1
                ja_flag = True
            dfs(i)
            candidate.remove(alpha[i])
            if mo_flag:
                mo -= 1
            if ja_flag:
                ja -= 1


dfs(-1)
for ans in answer:
    print(ans)
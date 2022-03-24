def count_unclear_player(stages, n):
    # n에 대해 count했을 때 일치하는 것의 갯수 return
    try:
        start = stages.index(n)
    except ValueError:
        return 0
    end_index = start
    for i in range(start, len(stages)):
        end_index = i
        if stages[i] > n:
            end_index = i - 1
            break
    return end_index - start + 1


def count_instage_player(stages, n):
    # n이상에 대해 count 한 것의 갯수 return
    try:
        start = stages.index(n)
    except ValueError:
        return 0
    return len(stages) - start


def solution(N, stages):
    answer = []
    for i in range(N):
        answer.append(list([0,i+1]))
    stages.sort()
    for i in range(1, len(answer) + 1):
        instage = count_instage_player(stages, i)
        unclear = count_unclear_player(stages, i)
        if instage == 0:
            answer[i - 1][0] = 0
        else:
            answer[i - 1][0] = unclear / instage
    answer.sort(key = lambda x: (-x[0], x[1]))
    result = list(map(lambda x: x[1], answer))
    return result

print(solution(5,[2,1,2,6,2,4,3,3]))
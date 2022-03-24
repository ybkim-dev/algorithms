n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

def dfs(i, num):
    global max_val, min_val
    if i == n:
       max_val = max(max_val, num)
       min_val = min(min_val, num)
    else:
        if operators[0] > 0:
            operators[0] -= 1
            dfs(i+1, num + nums[i])
            operators[0] += 1
        if operators[1] > 0:
            operators[1] -= 1
            dfs(i+1, num - nums[i])
            operators[1] += 1
        if operators[2] > 0:
            operators[2] -= 1
            dfs(i+1, num * nums[i])
            operators[2] += 1
        if operators[3] > 0:
            operators[3] -= 1
            dfs(i+1, int(num / nums[i]))
            operators[3] += 1

dfs(1, nums[0])

print(max_val)
print(min_val)

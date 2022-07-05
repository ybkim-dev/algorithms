from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = deque()
answer = ""
k = 0
for i in range(1, n+1):
    stack.append(i)
    answer += "+\n"
    for j in range(k,len(arr)):
        if len(stack) == 0: break
        temp = stack.pop()
        if arr[j] == temp:
            answer += "-\n"
            k = j + 1
        else:
            stack.append(temp)
            break


if len(stack) > 0:
    answer = "NO"

print(answer)
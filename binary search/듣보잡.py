N,M = map(int, input().split())

see = []
listen = []
for _ in range(N):
    listen.append(input())
for _ in range(M):
    see.append(input())

see.sort()
listen.sort()

def binary_search(arr, target, start, end):
    if start > end: return -1
    mid = (start + end) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: return binary_search(arr, target, mid+1, end)
    else: return binary_search(arr, target, start, mid- 1)
ans = 0
ans_arr=[]
for s in see:
    if binary_search(listen, s, 0, len(listen)- 1) >=0:
        ans += 1
        ans_arr.append(s)
    else: continue

print(ans)
for result in ans_arr:
    print(result)
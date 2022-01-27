# memoization list.
d = [0] * 100
d_bottom_up = [0] * 100

# top-down (재귀 방식)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    else:
        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

# bottom-up (for-loop 방식)
d_bottom_up[1] = 1
d_bottom_up[2] = 1
n = 99

for i in range(3,n+1):
    d_bottom_up[i] = d_bottom_up[i-2] + d_bottom_up[i-1]

print(d_bottom_up[n])

print(fibo(99))
n = int(input())

array = []
for i in range(n):
    array.append(input().split())
    array[i][1] = int(array[i][1])

array.sort(key=lambda x : x[1])

for i in array:
    print(i[0], end=" ")
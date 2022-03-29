from itertools import combinations

while True:
    line1 = list(map(int, input().split()))
    if line1[0] == 0:
        break
    N = line1[0]
    numbers = line1[1:]

    result = combinations(numbers, 6)
    for res in result:
        for i in res:
            print(i, end=" ")
        print()
    print()



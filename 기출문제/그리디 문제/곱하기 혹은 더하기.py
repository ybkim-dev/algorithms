# 곱연산 최대한 많이 수행하되, 0,1에 대해서는 더하기 연산 수행하면 최댓값 출력 가능

num_string = input()
num_int = []
for i in range(len(num_string)):
    num_int.append(int(num_string[i]))

result = 0
for num in num_int:
    if 0 <= num <= 1  or 0 <= result <= 1:
        result += num
    else:
        result *= num

print(result)
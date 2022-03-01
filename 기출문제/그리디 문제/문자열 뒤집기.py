# 1의 갯수, 0의 갯수 카운팅하여 적은 개수의 수(0 or 1)에 해당되는 덩어리 count

s = input()

zero_count = 0
one_count = 0

if s[0] == '1':
    one_count += 1
else:
    zero_count += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i] == '1':
            one_count += 1
        else:
            zero_count += 1

print(min(one_count, zero_count))
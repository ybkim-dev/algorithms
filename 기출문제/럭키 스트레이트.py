str_n = input()

left_sum = 0
right_sum = 0
for i in range(len(str_n)//2):
    left_sum += int(str_n[i])
    right_sum += int(str_n[len(str_n) - i - 1])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

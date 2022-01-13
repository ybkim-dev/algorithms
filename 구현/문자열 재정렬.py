s = input()

string_list = []
number_list = []
for i in range(len(s)):
    # 문자열이면 문자열 리스트에 담기
    if s[i].isalpha():
        string_list.append(s[i])
    # 숫자면 숫자 리스트에 담기
    else:
        number_list.append(s[i])

# 문자열 정렬
string_list.sort()
# 숫자 합
sum = 0
for number in number_list:
    sum += int(number)

for i in range(len(string_list)):
    print(string_list[i], end='')
print(sum)
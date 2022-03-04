sentence = input()

sum = 0
words = []
for word in sentence:
    if word.isdigit():
        sum += int(word)
    else:
        words.append(word)

words.sort()
for word in words:
    print(word,end='')
print(sum)
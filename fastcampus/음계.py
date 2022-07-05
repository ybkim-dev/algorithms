list =  list(map(int, input().split()))


ascending_cnt = 0
descending_cnt = 0

for i in range(len(list) - 1):
     if list[i] < list[i+1]:
         ascending_cnt+=1
     elif list[i] > list[i+1]:
         descending_cnt += 1

if ascending_cnt == 0:
    print("descending")
elif descending_cnt == 0:
    print("ascending")
else:
    print("mixed")
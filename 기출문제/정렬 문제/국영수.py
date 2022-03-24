n = int(input())

students = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    temp = dict()
    temp["name"] = name
    temp["kor"] = int(kor)
    temp["eng"] = int(eng)
    temp["mat"] = int(mat)
    students.append(temp)

students.sort(key = lambda x: (-x["kor"], x["eng"], -x["mat"], x["name"]))

for student in students:
    print(student["name"])
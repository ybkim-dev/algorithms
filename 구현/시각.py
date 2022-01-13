def main():
    # 3이 하나라도 포함되는 경우의 수 구하기
    n = int(input())

    count = 0
    # 0 ~ N 시 59분 59초까지 3이 포함되는 경우.
    for i in range(n+1):
        # 분
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)




if __name__ == "__main__":
    main()
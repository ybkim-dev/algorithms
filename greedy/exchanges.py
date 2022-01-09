def main():
    n = int(input())
    count =0

    coin_types = [500,100,50,10]

    for coin in coin_types:
        # 거슬러 줄 수 있는 동전의 개수를 높은 단위 순으로 나누어 count++
        count += n // coin
        # 거슬러 주고 남은 금액처리
        n %= coin

    print(count)

if __name__ == "__main__":
    main()
N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = []
max = -1
def card_selection(k):
    global max
    if k == 3:
        if sum(result) > max and sum(result) <= M:
            max = sum(result)
    else:
        for card in cards:
            if card not in result:
                result.append(card)
                card_selection(k+1)
                result.pop()
card_selection(0)
print(max)
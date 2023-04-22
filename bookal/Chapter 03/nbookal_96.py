# 2023-04-44 15:42 3분 컷
n, m = map(int, input().split())
card_input = [list(map(int, input().split())) for _ in range(n)]
min_list = [min(value) for value in card_input]
print(max(min_list))
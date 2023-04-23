# 2023-04-22 16:52 # 13분컷

input_pos = input()
current_pos = [0, 0]
chess_board = [
    [2, 3, 4, 4, 4, 4, 3, 2],
    [3, 4, 6, 6, 6, 6, 4, 3],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [4, 6, 8, 8, 8, 8, 6, 4],
    [3, 4, 6, 6, 6, 6, 4, 3],
    [2, 3, 4, 4, 4, 4, 3, 2]
]
row = ['a', 'b', 'c', 'd', 'e',' f',' g', 'h']

current_pos[0] = row.index(input_pos[0])-1
current_pos[1] = int(input_pos[1])-1

result = chess_board[current_pos[1]][current_pos[0]]
print(result)
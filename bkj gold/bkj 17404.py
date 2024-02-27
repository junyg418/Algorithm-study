class Node:
    def __init__(self, data:int, idx:int):
        self.data = data # 숫자값
        self.idx = idx   # 색상 0, 1, 2

t = int(input())

result_list = [[None] for _ in range(3)]

# 이진트리 root 초기화
temp = list(map(int, input().split()))
for idx, data in enumerate(temp):
    result_list[idx].append(Node(data, idx))

level = 1

# 전체 반복
for _ in range(t-1):
    temp = list(map(int, input().split()))

    # 3개의 완전 이진트리에 값 추가
    for node_idx in range(3):
        current_node_cnt = len(result_list[node_idx])
        # 각 데이터 노드에 데이터 추가
        for line in range(2**(level-1)):
            parent_node:Node = result_list[node_idx][2**(level-1)+line]


            # 자식 추가
            for idx, data in enumerate(temp):
                if parent_node.idx == idx:
                    continue
                result_list[node_idx].append(Node(parent_node.data+data, idx))

    level += 1

fin_list = []
for tree_cnt in range(3):
    while True:
        min_data:Node = min(result_list[tree_cnt][2**(level-1):], key=lambda x: x.data)
        if min_data.idx == tree_cnt:
            result_list[tree_cnt].remove(min_data)
            continue
        break
    fin_list.append(min_data)

print(min(fin_list, key=lambda x:x.data).data)
# 트리 노드의 개수 N
N = int(input())

# 인접리스트 생성
tree = [[] for _ in range(N)]

# 루트 노드는 따로 저장
root = None

# 각 노드의 부모를 입력 & 인접리스트로 연결
for child, parent in enumerate(map(int, input().split())):
    if parent == -1:
        root = child
        continue
    tree[parent].append(child)

# 삭제 노드 입력
remove = int(input())

for i in range(len(tree)):
    tree[i] = list(filter(lambda x: x != remove, tree[i]))

# 정답(리프노드의 개수)
answer = 0

# 깊이 우선 탐색
def dfs(node):
    global answer

    # 삭제된 노드인 경우
    if node == remove:
        return

    # 리프노드인 경우 (자식 X)
    if len(tree[node]) == 0:
        answer += 1
        return

    # 자식 노드들을 탐색
    for child in tree[node]:
        dfs(child)

# 루트에서부터 탐색
dfs(root)

# 정답출력
print(answer)

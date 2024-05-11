from collections import deque

v, e = map(int,input().split())
matrix = [[0 for i in range(v)]for j in range(v)]
print(matrix)

# [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

for _ in range(e):
    a,b = map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def DFS(matrix,start):
    visit = [False] * len(matrix)
    que = deque([start])

    while que:
        curr = que.popleft()
        if visit[curr]:
            continue
        visit[curr] = True
        print(f"{curr}정점 방문")
        for i in range(len(matrix[curr])):
            if not visit[i] and matrix[curr][i]:
                que.append(i)

DFS(matrix, 0)

# 0 1
# 0 2
# 0 4
# 1 2
# 2 3
# 3 4
# 2 4

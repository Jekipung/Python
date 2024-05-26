from collections import deque
import sys
input = sys.stdin.readline

v,e,s = map(int, input().split())
matrix = [[0] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
# 방문 표시 초기화, 0번째는 사용 x
visit = [False] * len(matrix)
def DFS(curr):
    visit[curr] = True
    print(curr, end=' ')

    for _next in range(1, len(matrix)):
        if not visit[_next] and matrix[curr][_next]:
            DFS(_next)


def BFS(start):
    que = deque()
    que.append(start)

    while que:
        curr = que.popleft()   # 현재 정점
        visit[curr] = True
        print(curr,end=" ")
        for _next in range(1, len(matrix)):
            if not visit[_next] and matrix[curr][_next]:
                que.append(_next)
                visit[_next] = True

DFS(s)
print()
visit = [False] * len(matrix)
BFS(s)

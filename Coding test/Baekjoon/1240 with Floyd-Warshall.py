# pypy3로 돌릴것.
import sys
s_input = sys.stdin.readline

# 노드의 개수 N, 노드 쌍의 개수 M
N, M = map(int, s_input().split())

# 최단거리 테이블 생성
d = [[float('inf')] * (N + 1) for _ in range(N + 1)]

# 연결된 두 점과 거리를 입력
for _ in range(N - 1):
    x, y, c = map(int, s_input().split())
    d[x][y] = d[y][x] = c

# 플로이드 워셜 수행
for m in range(N + 1):
    for x in range(N + 1):
        if d[x][m] == float('inf'):
            continue
        for y in range(N + 1):
            d[x][y] = min(d[x][y], d[x][m] + d[m][y])

# M개의 노드쌍에 대한 거리 출력
for _ in range(M):
    x, y = map(int, s_input().split())
    print(d[x][y])

"""
예제 입력 1
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
"""

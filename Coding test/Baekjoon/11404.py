import sys
input = sys.stdin.readline

# n개의 도시, m개의 버스(노선)
n = int(input())
m = int(input())

# 최소비용계산을 위한 리스트 생성
graph = [[float('inf')] * (n + 1) for _ in range(n+1)]
# 노선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 시작, 도착이 같은경우는 비용 0
for a in range(1, n + 1):
    graph[a][a] = 0

#  플로이드 워셜 수행
for m in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][m] + graph[m][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

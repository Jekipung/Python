import sys
input = sys.stdin.readline

# 지점의 개수 n, 골목길의 개수 m
n, m = map(int, input().split())

# 인접리스트 입력
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 최장거리 테이블
dist = [-float('inf') ]* (n + 1)
# 최적경로 테이블
path = [0] * (n + 1)

# 시작정점 설정
dist[1] = 0

# 벨먼포드 알고리즘 수행
for i in range(n):
    for u in range(1, n+1):
        for v, w in graph[u]:

            # 최대 비용, 최적경로 갱신
            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                path[v] = u

                # 갱신이 마지막 단계에서 발생하면 해당 정점을
                # 무한대로 갱신 -> 해당 경로에 사이클이 존재하면
                # 1 -> n 경로도 당연히 무한대가 될 것.
                if i == n - 1:
                    dist[v] = float('inf')
if dist[n] == float('inf'):
    print(-1)
else:
    u = n
    res = []
    while u != 1:
        res.append(u)
        u = path[u]
    res.append(u)
    print(*res[::-1], sep = ' ')


"""
예제 입력1

5 7
1 2 3
1 3 4
3 1 -7
2 3 2
3 4 1
4 2 -5
4 5 1

예제 출력1

1 2 3 4 5

"""

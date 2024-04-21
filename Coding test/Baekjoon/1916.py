import heapq
import sys

# 시간초과 방지용
input = sys.stdin.readline

N = int(input())  # 도시의 개수 N (정점)
M = int(input())  # 버스의 개수 M (간선)

# 인접리스트 생성
alist = [[] for _ in range(N + 1)]

# 인접리스트에 M개의 노선정보 입력
for _ in range(M):
    v1, v2, cost = map(int, input().split())
    alist[v1].append([cost, v2])

# 출발지(vertex start), 도착지(vertex end)
vs, ve = map(int, input().split())

# 최단거리, 방문표시 테이블 준비
dist = [float('inf')] * (N + 1)
visit = [False] * (N + 1)

# 우선순위 큐(최소 힙) 준비
pq = []

# 출발 노드 설정
heapq.heappush(pq, (0, vs))
dist[vs] = 0

while pq:
    # 가장 비용이 작은 노드 선택
    cost, v = heapq.heappop(pq)

    if visit[v]:
        continue
    visit[v] = True

    # v의 인접리스트 순회하며 최소비용 갱신
    for next_cost, target_v in alist[v]:
        if dist[target_v] > cost + next_cost:
            dist[target_v] = cost + next_cost
            heapq.heappush(pq, ( dist[target_v], target_v))

print(dist[ve])

"""
예제 입력1

5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

"""

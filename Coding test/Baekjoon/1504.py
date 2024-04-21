import heapq
import sys
input = sys.stdin.readline

# alist: 인접리스트
# start: 시작정점 번호
def dijkstra(alist, start):
    dist = [float('inf')] * len(alist)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        cost, v = heapq.heappop(pq)

        # 최근에 계산된 dist가 큐에서 꺼낸
        # 비용보다 작은 경우 무시
        if dist[v] < cost:
            continue

        for next_cost, target_v in alist[v]:
            if dist[target_v] > cost + next_cost:
                dist[target_v] = cost + next_cost
                heapq.heappush(pq, (dist[target_v], target_v))

    return dist


# 정점의 개수 n, 간선의 개수 e
n, e = map(int, input().split())

# 인접리스트 생성 및 a, b, c 값 양방향 대입
alist = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    alist[a].append([c, b])  # a -> b 비용 c
    alist[b].append([c, a])  # b -> a 비용 c

# 반드시 거쳐야 하는 정점 v1 과 v2
v1, v2 = map(int, input().split())

st_dist = dijkstra(alist, 1)  # 시작 정점에서 출발한 모든 최단 경로
v1_dist = dijkstra(alist, v1)     # v1에서 출발한 모든 최단 경로
v2_dist = dijkstra(alist, v2)     # v2에서 출발한 모든 최단 경로

st_v1_v2_n = st_dist[v1] + v1_dist[v2] + v2_dist[n]
st_v2_v1_n = st_dist[v2] + v2_dist[v1] + v1_dist[n]

result = min(st_v1_v2_n, st_v2_v1_n)
print(result if result != float('inf') else -1)

"""
예제 입력1

4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

"""

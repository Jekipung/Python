import heapq
import sys
input = sys.stdin.readline

# 한 줄에 들어가는 방의 수 n
n = int(input())

# 방의 구조
room = [list(input()[:-1]) for _ in range(n)]

# 최단거리 리스트를 초기화
dist = [[float('inf')] * n for _ in range(n)]

# 방문표시 리스트 초기화
visit = [[False] * n for _ in range(n)]

# 우선순위 큐 생성
pq = []

# 시간지점을 큐에 삽입 (비용, x, y)
heapq.heappush(pq,(0, 0, 0))
dist[0][0] = 0
while pq:
    # 비용이 제일 작은 노드 하나를 큐에서 pop
    cost, x, y = heapq.heappop(pq)

    # 방문한 노드면 건너뛰고 아니면 방문 표시
    if visit[x][y]:
        continue
    visit[x][y] = True
    # 상하좌우 노드 탐색
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        px = x + dx
        py = y + dy
        # 좌표 유효성 검사
        if 0 <= px < n and 0 <= py < n:
            pcost = cost + (0 if room[px][py] == '1' else 1)
            # 최소거리 갱신
            if dist[px][py] > pcost:
                dist[px][py] = pcost
                heapq.heappush(pq, (pcost, px, py))

print(dist[n-1][n-1]) # 정답 출력

"""
예제 입력1

8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111

"""
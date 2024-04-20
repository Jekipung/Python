import heapq

# 다익스트라 알고리즘 함수
# matrix: 가중치 인접 행렬
# start: 시작 노드
def dijkstra(matrix, start):
    # 1. 최단 거리 테이블 초기화, 방문 표시 테이블 초기화
    distance = [float('inf') for _ in range(len(matrix))]
    visit = [False for _ in range(len(matrix))]

    # 우선순위 큐 (최소 힙) 준비
    pq = []

    # 2. 출발 노드 설정 (간선 가중치와 노드 번호를 같이 넣어준다.)
    heapq.heappush(pq, (0, start))

    distance[start] = 0

    while pq:
        # 3. 방문하지 않은 가장 비용이 적은 node를 선택
        cost, node = heapq.heappop(pq)

        # 만약 이미 처리된 노드라면 넘어감
        if visit[node]:
            continue

        visit[node] = True

        # 4. 출발 노드 -> 선택 노드를 거쳐 가는 경우를 고려하여 최소 비용 갱신
        for i in range(len(matrix[node])):
            if distance[i] > matrix[node][i] + cost:
                distance[i] = matrix[node][i] + cost
                heapq.heappush(pq, (distance[i],i))

    return distance

inf = float('inf')
amatrix = [
    [0  , 3  , 4  , inf, inf, inf],
    [3  , 0  , inf, inf, 8  , inf],
    [4  , inf, 0  , 1  , 10 , inf],
    [inf, inf, 1  , 0  , inf, 2  ],
    [inf, 8  , 10 , inf, 0  , inf],
    [inf, 6  , inf, 2  , inf, 0  ]
]

dist = dijkstra(amatrix, 0)
print(dist)

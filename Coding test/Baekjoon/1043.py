# 진실을 아는 사람들이 있는 파티는 거짓말 x
# 진실을 아는 사람들이 있는 파티에서는 진실을 알게됨
# 진실을 모르는 사람들로만 이루어진 파티를 찾을것

# 사람들이 진실을 알게되는 경우의 수를 모두 찾아낸다.
# 진실을 알지 못하는 경우만 카운트 한다.

from collections import deque

# 사람의 수 N, 파티의 수 M
N, M = map(int, input().split())

# 진실을 아는 사람들의 번호 K
# 사람의 수는 len() 메서드로 대체 가능하기에 slicing을 통해 잘라낸다.
K = list(map(int, input().split()))[1:]

# 파티 참여정보 P
# 위와 동일한 이유로 잘라낸다.
P = []
for _ in range(M):
    P.append(list(map(int, input().split()))[1:])

# BFS 큐 준비
q = deque(K) # q라는 queue에 K가 전부 들어감.
# 진실을 아는 사람들의 방문처리 리스트
v_person = [False] * (N + 1) # (N+1의 이유는 사람의 번호는 1부터 시작하기 때문)
# 진시을 아는 파티의 방문처리 리스트
v_party = [False] * M

# BFS 알고리즘을 통해 진실을 알게되는 모든 경우를 탐색
while q: # q가 존재할때
    x = q.popleft() # x는 q의 왼쪽부터
    v_person[x] =  True # x번 진실을 아는 사람의 방문처리

    # 모든 파티에 대해 탐색
    for i in range(M):
        # 진실을 아는 사람들이 있는 파티
        if x in P[i]:
            v_party[i] = True # i번 진실을 아는 사람들이 있는 파티 방문처리

            # 그로인해 진실을 알게된 사람들
            for y in P[i]:
                if not v_person[y] and x != y:
                    q.append(y)
                    v_person[y] = True

# 진실을 모르는 파티만 카운트
print(v_party.count(False))

"""
예제 입력 4

4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
"""

"""
예제 출력 4

2
"""

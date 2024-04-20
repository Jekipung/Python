import sys
input = sys.stdin.readline

# 사람의 수 N
N = int(input())

# 친구 관계 테이블 (N * N)
rel = [list(input()) for _ in range(N)]

# 2-친구 관계 테이블 (N * N)
two_rel = [[0] * N for _ in range(N)]

# 1. 자신과 친구가 될 수 없음 -> 0
# 2. A와 B가 친구임 -> 1
# 3. A와 C가 친구고, C와 B가 친구임 -> 1
for c in range(N):
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            if rel[a][b] == 'Y':
                two_rel[a][b] = 1
            if rel[a][c] == 'Y' and rel[c][b] == 'Y':
                two_rel[a][b] = 1

answer = 0
for r in two_rel:
    answer = max(answer, sum(r))
print(answer)

"""
예제입력 1
3
NYY
YNY
YYN

예제출력 1
2
"""

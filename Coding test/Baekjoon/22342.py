import sys
input = sys.stdin.readline
# 각 로봇들의 저장값 중 가장 큰 값을 출력
# 로봇은 하나 이상의 입력값, 하나의 저장값, 하나의 출력값을 가진다.
# 제일 왼쪽 열에있는 로봇의 입력값은 0 하나다.
# (i, j)에 위치한 로봇의 입력값은 |i−a| ≤ j −b, b < j인 모든 좌표 (a, b)에 있는 로봇들의 출력 값들이다.
# 저장값은 입력값들 중 가장 큰 값이다.
# 출력값은 저장값 + 가중치(i, j)의 값이다.
m, n = map(int, input().split())

# 가중치 값들
weights = []
for i in range(n):
    weights.append(list(map(int, input().strip())))

# 로봇이 들어있는 행렬
metrix = [[0]]


import sys
input = sys.stdin.readline

n,m = map(int,input().split())

weights = []
for i in range(n):
    weights.append(list(map(int,input().strip())))

matrix =[[0 for i in range(m+1)] for j in range(n+2)]
answer = 0

for x in range(1,m+1):
    for y in range(1,n+1):
        store = max(matrix[y - 1][x - 1], matrix[y][x - 1], matrix[y + 1][x - 1])
        if answer < store :
            answer = store
        matrix[y][x] = store + weights[y-1][x-1]

print(answer)

"""
예제 입력1
3 4
1234
2341
3412
"""

"""
예제 출력 1
11
"""

from collections import deque
def solution(maps):
    # 시작점: 0,0
    Que = deque()
    # r: 행의 길이, c: 열의 길이
    r, c = len(maps), len(maps[0])
    target = [r-1, c-1] # 목적지
    visit = [[False] * c for _ in range(r)]
    Que.append([0,0,1])
    visit[0][0] = True

    while Que:
        x, y, cnt = Que.popleft()
        if [x, y] == target: return cnt
        for nx, ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if 0 <= nx < r and 0 <= ny < c:
                if not visit[nx][ny] and maps[nx][ny]:
                    Que.append([nx, ny, cnt+1])
                    visit[nx][ny] = True


    return - 1

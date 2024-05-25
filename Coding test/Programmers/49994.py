def solution(dirs):
    # 가로, 세로 길이가 10인 좌표평면에서 처음 이동한 거리의 길이를 리턴하라.
    # 처음 이동한 거리를 구하기 위해서는 매번 이동한 길에 대해 기록
    offset = {"U": (-1,0), "D": (1, 0), "R": (0, -1), "L": (0, 1)}
    x, y = 0,0   # 현재 좌표
    path = set()
    for d in dirs:
        nx, ny = offset[d]
        nx += x
        ny += y
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path.add((x, y, nx, ny))   # 현재 좌표에서 다음 좌표로 이동했다는 것을 기록
            path.add((nx, ny, x, y))   # 반대로 이동했을 경우도 기록
            x, y = nx, ny

    return len(path) // 2

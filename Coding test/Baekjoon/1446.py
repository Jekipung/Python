def teacher():
    N, D = map(int, input().split())
    shortcut = {}
    for _ in range(N):
        start, end, length, = map(int, input().split())
        # 목표지점 D보다 작은 경우에만 저장 (D보다 더 멀리 갈 수 없음)
        if end <= D:
            if start not in shortcut:
                shortcut[start] = [(end, length)]
            else:
                shortcut[start].append((end, length))

    # 각 위치의 최단 거리
    dp = [float("inf")] * (D + 1)
    dp[0] = 0

    # DP를 사용하여 각 위치까지의 최단거리 갱신
    for i in range(D + 1):
        # 현재 i 까지 거리 vs i - 1 까지 거리 + 1
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)

        # i에 지름길이 있다면 다음 위치 미리 갱신
        if i in shortcut:
            for end, length in shortcut[i]:
                dp[end] = min(dp[end], dp[i] + length)

    # 목표지점까지의 거리 출력
    print(dp[D])

def student():
    # 점화식 dp[i] = min(dp[i], dp[i - 1] + 1)
    n, d = map(int, input().split())
    dp = [0]
    dp += [float("inf")] * (d)
    fast_road = []
    for i in range(n):
        fast_road.append(list(map(int, input().split())))
    for i in range(d + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        for j in fast_road:
            if i == j[0] and d >= j[1]:
                dp[j[1]] = min(dp[j[1]], dp[i] + j[2])
    print(dp[d])

teacher()
student()

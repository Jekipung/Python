# 사람의 수 N
N = int(input())
# 각 사람에게 인사시 잃는 체력 L
L = [0] + list(map(int, input().split()))
# 각 사람에게 인사시 얻는 기쁨 J
J = [0] + list(map(int, input().split()))

# DP 처리용 리스트 (기쁨 [사람] [체력])
dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):   # i번 사람
    for j in range(1, 101): # 체력 j
        if L[i] <= j:
            # i번 사람에게 인사가 가능한 경우
            # 기쁨[사람][체력] = max[기쁨][이전사람][체력], 기쁨[이전사람][체력 - 소모체력] + 얻는기쁨
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][99])

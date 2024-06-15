# n개의 동전, 구매하고자 하는 가치의 합 k
n,k = map(int, input().split())

# 동전의 종류(가치)
coin = [int(input()) for _ in range(n)]

# 각 금액을 만드는데 필요한 동전의 개수들
dp = [10001] * (k + 1)
dp[0] = 0

for coin_value in coin:
    # 선택한 동전으로 각 금액에 대한 동전개수 업데이트
    for i in range(coin_value, k + 1):
        # 현재 금액 i를 만들기 위해 필요한 동전의 개수 dp[i]
        # 선택 동전을 사용할 경우 dp[i - coin_value] + 1 비교
        dp[i] = min(dp[i], dp[i - coin_value] + 1)

# 정답 출력
print(dp[k] if dp[k] != 10001 else -1)

"""
예제 입력 1
3 15
1
5
12
"""

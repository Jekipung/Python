import sys
input = sys.stdin.readline

n = int(input())   # 정수의 개수
nums = list(map(int, input().split()))   # 정수 리스트
k = int(input())   # 최대로 사용가능한 정수의 개수

# [1 - 최대값] dp 리스트
max_len = nums[-1] * k + 2
dp = [float('inf')] * max_len

# nums에 있는 값들은 모두 1로 초기화
for num in nums:
    dp[num] = 1
for i in range(1, len(dp)):
    # i보다 숫자 j들로 i를 만들 수 있다
    # ex) 5 => (1 + 4), (2 + 3)
    for j in range(1, i // 2 + 1):
        # j를 쓰는 경우가 현재 i를 만드는 경우보다 더 적으면 업데이트
        dp[i] = min(dp[i], dp[j] + dp[i - j])

    # i를 만드는 경우가 k개를 넘어가면 패배
    if dp[i] > k:
        print("holsoon" if i % 2 == 0 else "jjaksoon", end=' ')
        print("win at", i)
        break

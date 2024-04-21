N, S = map(int, input().split())         # N: 입력받을 정수의 수, S: 티켓
nums = list(map(int, input().split()))   # 입력받은 정수들
v = [False] * (N + 1)                    # 방문 표시 v 생성
answer = 0                               # 정답의 개수

def recursion(idx, summery):
    global answer
    if idx == N:                         # 봐야 할 정수를 모두 보았으므로 돌아간다.
        return answer
    summery += nums[idx]                 # 합계 계산
    if summery == S:
        answer += 1

    recursion(idx + 1, summery)
    recursion(idx + 1, summery - nums[idx])


recursion(0, 0)
print(answer)

"""
예제 입력1

5 0
-7 -3 -2 5 8

"""

import sys
sys.setrecursionlimit(10000001)

# 이전값 저장 cache
cache = {}

# 피보나치 수열 n번째 항 재귀함수
def f(n):
    # 기본 처리
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 캐시에서 먼저 확인
    if n in cache:
        return cache[n]
    else:
        cache[n] = (f(n - 1) + f(n - 2)) % 1000000000
        return cache[n]

n = int(input())

# 결과
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(f(abs(n)))

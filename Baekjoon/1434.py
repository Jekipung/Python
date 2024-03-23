# input 입력 시간을 단축하기 위한 코드
import sys
input = sys.stdin.readline

# 첫째줄에는 박스와 책의 갯수 정수 n,b
n,b = map(int, input().split())
# 둘째줄에는 박스의 크기가 담긴 리스트
A = list(map(int, input().split()))
# 셋째줄에는 책의 크기가 담긴 리스트
B = list(map(int, input().split()))
# 낭비된 박스 공간


waste = 0
i, j = 0,0
while i < n :
    if A[i] >= B[j]:
        A[i] -= B[j]
        j += 1
        if j >= b:
            waste += sum(A[i:])
            break
    else:
        waste += A[i]
        i += 1
print(waste)

"""
예제 입력1

3 3
5 5 5
5 5 5

"""

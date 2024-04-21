# 중간지점의 개수 N
N = int(input())
# 중간지점의 속력제한 course
course = list(map(int, input().split()))
# 성과 result
result = 0
v = 0
for c in course[::-1]:
    v += 1
    v = min(v,c)
    result += v
print(result)

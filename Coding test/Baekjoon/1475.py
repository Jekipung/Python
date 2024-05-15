N = list(map(int, input()))
List = [0] * 10


for i in N: # N = 받은 숫자열, i = 숫자열에서 뽑아온 숫자
    List[i] += 1
v = List[6] + List.pop()
if v % 2 != 0:
    v += 1
List[6] = v // 2
print(max(List))

# 소문자로 이루어진 문자열을 입력받고,
# 입력받은 문자열을 임의로 3등분 한다.
# 3등분한 문자열을 각각 뒤집고,
# 다시 원래의 순서대로 합첬을때,
# 사전순으로 가장 앞서는 단어를 출력한다.
# 문자열끼리 비교할경우 사전순으로 앞설수록 크다.
# ex) a는 b보다 크고, b는 c보다 크다.
#

String = input()
words = []
for i in range(len(String)-1, 1, -1):
    for j in range(i-1,0,-1):
        words.append(''.join([String[j-1::-1],String[i-1:j-1:-1],String[:i-1:-1]]))
words.sort()
print(words[0])

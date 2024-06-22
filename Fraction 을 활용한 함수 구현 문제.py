from fractions import Fraction
def word_fraction(string:str, frac:Fraction):
    a,b  = frac.as_integer_ratio()
    if len(string) % b != 0:
        raise AssertionError("invalid fracion")
    a *= len(string) // b
    if a < 0: result = string[a:]
    else:  result = string[:a]
    return result
# combine 함수
# 두 개의 리스트를 입력으로 받아 처리한다.
# 첫번째 리스트는 단어들을 포함한 리스트
# 두번째 리스트는 fraction들을 포함한 리스트
# 결과값: 각 단어와 해당하는 분수를 조합하여 생성된 문자열
def combine(strings: list, fracs: list):
    result = ""
    for i in range(len(strings)):
        result += word_fraction(strings[i], fracs[i])
    return result
# decompose 함수
# 질문 문자열을 입력으로 받아 처리
# 결과값: 두개의요소를 가진 튜플을 반환
#       첫번째 요소: 질문에서 추출한 모든 단어들을 포함하는 리스트
#       두번 째 요소: 질문에서 추출한 모든 분수(fraction)을 포함하는 리스트
def decompose(query):
    parse = query.replace('What is ','').replace(',','').replace('and ','').replace('?','')
    parse = parse.split()
    result1 = []
    result2 = []
    for i in range(0,len(parse),2):
        frac_a,frac_b = map(int,parse[i].split('/'))
        result2.append(Fraction(frac_a,frac_b))
        result1.append(parse[i+1])
    return result1,result2
# answer: 질문 문자열을 입력으로 받아 처리하는 함수
# 질문에 포함된 단어와 분수들을 기반으로 각 단어와 해당 분수를 조합하여 생성된 문자열 반환
# 예외처리: 함수 word_fraction, combine 또는 answer를 호출할 때 불가능한
# 단어 분수(ex: spam에서 3/5 글자를 선택하는 것은 불가능)=> AssrtionError를 발생
# 에러 메시지는 "invalid fraction" 이라고 나타내면 된다.
def answer(query):
    strings, fracs = decompose(query)
    return combine(strings,fracs)

print(word_fraction('wallaby', Fraction(4, 7)))
'wall'
print(word_fraction('parakeet', Fraction(2, 8)))
'pa'
print(word_fraction('perch', Fraction(3, 5)))
'per'
print(word_fraction('ALPACA', Fraction(-1, 3)))
'CA'
print(word_fraction('PARTRIDGE', Fraction(-7, 9)))
'RTRIDGE'
print(word_fraction('manatee', Fraction(1, 2)))
# Traceback (most recent call last):
# AssertionError: invalid fraction

print(combine(['wallaby', 'parakeet', 'perch'], [Fraction(4, 7), Fraction(1, 4), Fraction(3,5)]))
'wallpaper'
print(combine(['ALPACA', 'PARTRIDGE'], [Fraction(-1, 3), Fraction(-7, 9)]))
'CARTRIDGE'
print(combine(['Manatee', 'cheetah', 'hamster'], [Fraction(3, 7), Fraction(3, 7), Fraction(-4, 7)]))
'Manchester'
print(decompose('What is 4/7 wallaby, 1/4 parakeet and 3/5 perch?')
(['wallaby', 'parakeet', 'perch'], [Fraction(4, 7), Fraction(1, 4), Fraction(3, 5)]))
print(decompose('What is -1/3 ALPACA and -7/9 PARTRIDGE?')
(['ALPACA', 'PARTRIDGE'], [Fraction(-1, 3), Fraction(-7, 9)]))
print(decompose('What is 3/7 Manatee, 3/7 cheetah and -4/7 hamster?')
(['Manatee', 'cheetah', 'hamster'], [Fraction(3, 7), Fraction(3, 7), Fraction(-4, 7)]))
print(answer('What is 4/7 wallaby, 1/4 parakeet and 3/5 perch?'))
'wallpaper'
print(answer('What is -1/3 ALPACA and -7/9 PARTRIDGE?'))
'CARTRIDGE'
print(answer('What is 3/7 Manatee, 3/7 cheetah and -4/7 hamster?'))
'Manchester'

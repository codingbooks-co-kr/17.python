# ❷ 숫자 문자열에 map() 함수를 적용한 예
words = "10 20 30"	# 또는 words = input("숫자열: ")

# 문자열을 공백으로 분리한 후 각 숫자문자를 정수로 변환
result = map(int, words.split())
print(list(result))

# 문자열을 공백으로 분리한 후 각 숫자문자를 정수*2로 변환
result = map(lambda x: int(x) * 2, words.split())
print(list(result))
# ❷ 숫자 문자열에 리스트 함축을 적용한 예
words = "10 20 30"	# words = input("숫자열: ")

# 문자열을 공백으로 분리한 후 각 숫자문자를 정수로 변환
result = [int(x) for x in words.split()]
print(result)

# 문자열을 공백으로 분리한 후 각 숫자문자를 정수*2로 변환
result = [int(x) * 2 for x in words.split()]
print(result)
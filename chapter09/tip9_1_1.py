# ❶ 문자열(=문자의 집합)에 리스트 함축을 적용한 예
words = "apple"		# words = input("문자열: ")

# 문자열의 각 문자 요소를 대문자로 변환
result = [x.upper() for x in words]
print(result)

# 문자열의 각 문자가 'p'와 같으면 True, 아니면 False로 변환
result = [x == 'p' for x in words]
print(result)
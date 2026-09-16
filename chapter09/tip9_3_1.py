# ❶ 문자열(=문자의 집합)에 리스트 함축을 적용한 예
words = "python123"	# words = input("문자열: ")

# 문자열의 각 문자 요소 중 알파벳만 필터링
result = [x for x in words if x.isalpha()]
print(result)

# 문자열의 각 문자 요소 중 숫자만 필터링
result = [x for x in words if x.isdigit()]
print(result)
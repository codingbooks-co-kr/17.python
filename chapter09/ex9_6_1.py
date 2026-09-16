# ❶ 문자열(=문자의 집합)에 filter() 함수를 적용한 예
words = "python123"	# 또는 words = input("문자열: ")

# 문자열의 각 문자 요소 중 알파벳만 필터링
result = filter(str.isalpha, words)
print(result)	# filter 객체
print(list(result))	# 객체→리스트 변환

# 문자열의 각 문자 요소 중 숫자만 필터링
result = filter(str.isdigit, words)
print(list(result))
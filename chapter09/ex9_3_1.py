# ❶ 문자열(=문자의 집합)에 map() 함수를 적용한 예
words = "apple"		# 또는 words = input("문자열: ")

# 문자열의 각 문자 요소를 대문자로 변환
result = map(str.upper, words)
print(result)		# map 객체
print(list(result))		# map 객체→리스트 변환

# 문자열의 각 문자가 'p'와 같으면 True, 아니면 False로 변환
result = map(lambda x: x == 'p', words)
print(list(result))		# 결과를 리스트로 변환
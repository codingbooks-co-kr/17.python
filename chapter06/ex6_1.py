# 문자열의 덧셈(연결), 곱셈(반복) 연산

words1 = "Python"
words2 = "Coding"
num = 123

# [1] 문자열 덧셈 연산 (연결하기)
print(words1 + str(num))		# 숫자를 문자로 형변환 후 연결
print(words1 + words2)		# 문자열 덧셈(연결)
print(words1 + " " + words2)		# 중간에 공백문자 삽입

# 문자열 복합 할당 연산자(+=) 사용하기
words = "Hello"
words += " "			# 문자열 덧셈(복합할당연산)
words += "Python"			# 문자열 덧셈(복합할당연산)
print(words)

print("20" + "20")			# 문자열 덧셈(연결)
print("Hello" + "Python")		# 문자열 덧셈(연결)
print("나이: " + str(20) + "세")		# 문자열 덧셈(연결)
print("체온: " + str(36.5) + "도")	# 문자열 덧셈(연결)

# [2] 문자열 곱셈 연산 (반복하기)
print(words1 * 3)			# 문자열 곱셈(반복)
print("파이썬" * 3)			# 문자열 곱셈(반복)
print(3 * "파이썬")			# 문자열 곱셈(반복)
print("#" * 10)			# 문자열 곱셈(반복)
print(10 * "#")			# 문자열 곱셈(반복)

# 문자열 복합 할당 연산자(*=) 사용하기
words = "Python"	
words *= 3			# 문자열 곱셈(복합할당연산)
print(words)
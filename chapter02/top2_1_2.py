# ❶ int()를 사용한 정수 변환: 실수/정수문자열을 정수로 변환
print(int(3.14))		# 실수→정수 변환 (소수점 이하 버림)
print(int("123"))		# 정수문자열→정수 변환
#print(int("3.14"))		# 실수문자열→정수 변환 오류(ValueError)
#print(int("Python"))		# 일반문자열→정수 변환 오류(ValueError)

# ❷ float()를 사용한 실수 변환: 정수/숫자문자열을 실수로 변환
print(float(10))		# 정수→실수 변환
print(float("3.14"))		# 실수문자열→실수 변환
print(float("123"))		# 정수문자열→실수 변환
#print(float("12 3"))		# 숫자 사이에 문자(공백) 있으면 오류(ValueError)
#print(float("Python"))	# 일반문자열→실수 변환 오류(ValueError)

# ❸ str()을 사용한 문자열 변환: 숫자/True/False/None을 문자열로 변환
print(str(10))		# 정수→문자열 변환 (화면 출력 시 따옴표 안보임)
print(str(3.14))		# 실수→문자열 변환 (화면 출력 시 따옴표 안보임)
print(str(True))		# True→문자열 변환 (화면 출력 시 따옴표 안보임)
print(str(False))		# False→문자열 변환 (화면 출력 시 따옴표 안보임)
print(str(None))		# None→문자열 변환 (화면 출력 시 따옴표 안보임)

# 중첩 변환 팁: 실수문자열→실수→정수 변환
# 1단계 변환: float("3.14") → 3.14 (실수)	
# 2단계 변환: int(3.14) → 3 (정수)
print(int(float("3.14")))	# 실수문자열→실수→정수 변환
#print(int("3.14"))		# 실수문자열→정수 변환은 오류(ValueError)
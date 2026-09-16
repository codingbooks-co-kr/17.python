import math		# math 모듈 불러오기

print(math.pi)		# 원주율(π) 상수 사용
print(math.e)		# 자연로그의 밑(e)
print(math.exp(1))		# e의 1제곱 (math.e**1과 동일)
print(math.sqrt(4))		# 4의 제곱근(√4)

print(math.pow(4, 0.5))	# 거듭제곱(40.5): 4의 0.5제곱(제곱근)
print(math.pow(2, 3))	# 거듭제곱(2³): 2의 3제곱 (2**3와 동일)

print(math.factorial(5))	# 팩토리얼(5! = 5*4*3*2*1 = 120)

print(math.log(8, 2))		# print(math.log2(8)): 밑이 2인 로그(log28)
print(math.log(100, 10))	# print(math.log10(100)): 밑이 10인 로그(log10100)
print(math.log(100, math.e))	# print(math.log(100)): 밑이 e인 자연로그

print(math.ceil(3.14))	# 실수(올림) → 정수 반환
print(math.ceil(-3.14))
print(math.floor(3.14))	# 실수(내림) → 정수 반환
print(math.floor(-3.14))

print(round(3.14159))    	# 정수로 반올림, round()는 파이썬 내장 함수
print(round(3.6))        	# 정수로 반올림, round()는 파이썬 내장 함수 
print(round(3.14159, 2)) 	# 소수점 둘째 자리까지 반올림

rad = math.radians(90)	# 90도 → 라디안값 반환
print(math.sin(rad))		# sin(라디안값)
print(math.sin(math.pi/2))	# sin(라디안값)
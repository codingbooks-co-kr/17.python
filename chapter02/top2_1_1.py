# 동일 변수(data)에 다양한 자료형으로 재할당

data = 10			# 숫자형: 정수(int)
print(data, type(data))

data = 3.14		# 숫자형: 실수(float)
print(data, type(data))

data = 3+4j		# 숫자형: 복소수(complex)
print(data, type(data))

data = True		# 불리언형(bool)
print(data, type(data))

data = "Python"		# 시퀀스형: 문자열(str)
print(data, type(data))

data = [1, 2, 3]		# 시퀀스형: 리스트(list)
print(data, type(data))

data = (1, 2, 3)		# 시퀀스형: 튜플(tuple)
print(data, type(data))

data = {'a': 1, 'b': 2}	# 매핑형: 딕셔너리(dict)
print(data, type(data))

data = {1, 2, 3}		# 세트형(set)
print(data, type(data))

data = None		# None형
print(data, type(data))
# 딕셔너리 관련 다양한 내장 함수

fruits = {"apple": 1000, "kiwi": 2500, "cherry": 5000}
print(len(fruits))			# 딕셔너리 항목 개수
print(min(fruits))			# 키가 (사전순) 최소인 키
print(max(fruits))			# 키가 (사전순) 최대인 키
print(min(fruits, key=fruits.get))	# 값이 (크기순) 최소인 키
print(max(fruits, key=fruits.get))	# 값이 (크기순) 최대인 키
print(sorted(fruits))			# 키 기준 정렬(사전순)
print(sorted(fruits, key=fruits.get))	# 값 기준 정렬(크기순)
print(sorted(fruits, key=fruits.get, reverse=True))	# 역순
# print(sum(fruits))		# 키들의 합계 (키가 숫자인 경우만 가능)
print(sum(fruits.values()))	# 값들의 합계
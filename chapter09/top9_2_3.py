# 이터레이터를 반환하는 고차 함수(map, filter 등) 사용 시 주의점

nums = [1, 2, 3, 4, 5]			# 원본 데이터
result1 = map(lambda x: x ** 2, nums)		# map() 적용 후 result1은 이터레이터 객체
print(list(result1))				# ❶ 결과: [1, 4, 9, 16, 25]
print(list(result1))				# ❷ 결과 (데이터 이미 바닥남): []
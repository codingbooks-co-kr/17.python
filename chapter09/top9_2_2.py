# ❷ 람다 함수와 고차 함수를 활용한 함수형 프로그래밍

from functools import reduce

# 원본 데이터
nums = [1, 2, 3, 4, 5]
print(f"원본 데이터: {nums}")		# 원본 데이터

# 1단계: 각 숫자를 제곱으로 변환 (람다 함수 사용)
result1 = list(map(lambda x: x ** 2, nums))
print(f"1단계(map): {result1}")		# map() 적용

# 2단계: 짝수만 필터링 (람다 함수 사용)
result2 = list(filter(lambda x: x % 2 == 0, result1))
print(f"2단계(filter): {result2}")		# filter() 적용

# 3단계: 값 누적 (람다 함수 사용)
result3 = reduce(lambda x, y: x + y, result2)
print(f"3단계(reduce): {result3}")	# reduce() 적용
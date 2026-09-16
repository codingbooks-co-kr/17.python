# ❶ 순수 함수와 고차 함수를 활용한 함수형 프로그래밍

from functools import reduce

nums = [1, 2, 3, 4, 5]	# 원본 데이터

def get_square(x):		# 제곱 반환 함수
    return x ** 2

def is_even(x):		# 짝수 반환 함수
    return x % 2 == 0

def get_addition(x, y):	# 덧셈 반환 함수
    return x + y

print(f"원본 데이터: {nums}")	# 원본 데이터 출력

# 1단계: map()을 적용해서 각 숫자를 제곱으로 변환
result1 = list(map(get_square, nums))
print(f"1단계(map): {result1}")		# map() 적용

# 2단계: filter()를 적용해서 짝수만 추출(필터링)
result2 = list(filter(is_even, result1))
print(f"2단계(filter): {result2}")		# filter() 적용

# 3단계: reduce()를 적용해서 값 누적
result3 = reduce(get_addition, result2)
print(f"3단계(reduce): {result3}")	# reduce() 적용
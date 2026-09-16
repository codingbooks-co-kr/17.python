# ❸ 숫자 리스트에 map() 함수를 적용한 예 
nums = [1, 2, 3, 4, 5]

# 리스트의 숫자 요소를 제곱으로 변환 (람다함수 사용)
result = map(lambda x: x ** 2, nums)
print(list(result))

# 리스트의 숫자 요소가 짝수이면 True, 홀수이면 False로 변환
result = map(lambda x: x % 2 == 0, nums)
print(list(result))
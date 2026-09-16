# ❸ 숫자 리스트에 리스트 함축을 적용한 예
nums = [1, 2, 3, 4, 5]

# 리스트의 숫자 요소를 제곱으로 변환
result = [x ** 2 for x in nums]
print(result)

# 리스트의 숫자 요소가 짝수이면 True, 홀수이면 False로 변환
result = [x % 2 == 0 for x in nums]
print(result)
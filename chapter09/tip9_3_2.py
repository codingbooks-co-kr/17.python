# ❷ 숫자 리스트에 리스트 함축을 적용한 예
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 숫자 리스트의 요소 중 짝수만 필터링
result = [x for x in nums if x % 2 == 0]
print(result)

# 숫자 리스트의 요소 중 6 이상만 필터링
result = [x for x in nums if x >= 6]
print(result)
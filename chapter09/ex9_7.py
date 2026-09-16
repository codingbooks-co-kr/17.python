# functools 모듈로부터 reduce() 함수 가져오기
from functools import reduce

# ❶ 숫자 리스트의 모든 요소의 누적합 → 대체: result = sum(nums)
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)

# ❷ 숫자 리스트의 모든 요소의 누적합 (초기값은 100)
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums, 100)
print(result)

# ❸ 숫자 리스트의 모든 요소의 누적곱
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, nums)
print(result)

# ❹ 문자열 리스트의 요소 길이의 누적합 (초기값은 0)
words = ["apple", "banana", "kiwi", "watermelon"]
result = reduce(lambda x, y: x + len(y), words, 0)
print(result)

# ❺ 리스트의 요소 중 최댓값 구하기 → 대체: result = max(nums)
nums = [1, 5, 2, 7, 4]
result = reduce(lambda x, y: x if x > y else y, nums)
print(result)
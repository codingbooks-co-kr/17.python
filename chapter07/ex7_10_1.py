# 리스트 숫자 요소의 오름차순 정렬
nums = [3, 5, 2, 1, 4]
result = sorted(nums)
print(result)

# 리스트 숫자 요소의 내림차순 정렬
nums = [3, 5, 2, 1, 4]
result = sorted(nums, reverse=True)
print(result)

# 리스트 숫자 요소의 절댓값을 기준으로 오름차순 정렬
nums = [10, -7, 3, -13, -9, 1]
result = sorted(nums, key=abs)
print(result)

# 리스트 문자열 요소의 길이를 기준으로 오름차순 정렬
fruits = ["banana", "kiwi", "avocado", "apple"]
result = sorted(fruits, key=len)
print(result)

# 리스트 문자열 요소의 소문자를 기준으로 오름차순 정렬
fruits = ["banana", "kiwi", "Avocado", "apple"]
result = sorted(fruits, key=str.lower)
print(result)
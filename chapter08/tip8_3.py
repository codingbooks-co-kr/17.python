# 쉼표로 구분된 여러 값 중에서 가장 작은/큰 값 찾기
print(min(2, 9, 1, 5))		# 크기순
print(min("banana", "apple", "kiwi"))	# 사전순
print(max(2, 9, 1, 5))		# 크기순
print(max("banana", "apple", "kiwi"))	# 사전순

nums = [2, 9, 1, 5]
print(min(nums))
print(max(nums))

# 길이를 기준으로 가장 짧은 단어 찾기
words = ["Apple", "Banana", "Kiwi"]
print(min(words, key=len))
print(max(words, key=len))

# 대소문자 무시하고 사전순으로 가장 작은/큰 단어 찾기
print(min(words, key=str.lower))
print(max(words, key=str.lower))

# 절댓값을 기준으로 가장 작은/큰 값 찾기
nums = [1, -5, 4, -9, -7, 2]
print(min(nums, key=abs))
print(max(nums, key=abs))
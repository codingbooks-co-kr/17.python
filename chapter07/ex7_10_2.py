# 리스트 숫자 요소의 오름차순 정렬 (원본 리스트 변경)
nums = [3, 5, 2, 1, 4]
nums.sort()	
print(nums)

# 리스트 숫자 요소의 내림차순 정렬 (원본 리스트 변경)
nums = [3, 5, 2, 1, 4]
nums.sort(reverse=True)	
print(nums)

# 리스트 숫자 요소의 절댓값 기준 오름차순 정렬 (원본 리스트 변경)
nums = [10, -7, 3, -13, -9, 1]
nums.sort(key=abs)
print(nums)

# 리스트 문자열 요소의 길이 기준 오름차순 정렬 (원본 리스트 변경)
fruits = ["banana", "kiwi", "avocado", "apple"]
fruits.sort(key=len)
print(fruits) 

# 리스트 문자열 요소의 소문자 기준 오름차순 정렬 (원본 리스트 변경)
fruits = ["banana", "kiwi", "Avocado", "apple"]
fruits.sort(key=str.lower)
print(fruits) 
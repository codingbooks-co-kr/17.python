# 리스트의 인덱싱(Indexing), 슬라이싱(Slicing)

nums = [1, 2, 3, 4, 5, 6]

# [1] 인덱싱(Indexing): 단일 요소 조회
print(nums[0])		# 인덱스 0번 요소
print(nums[3])		# 인덱스 3번 요소
print(nums[-1])		# 끝 요소
print(nums[-3])		# 끝에서 3번째 요소

# [2] 슬라이싱(Slicing): 범위 잘라내기 [시작:끝:간격]
print(nums[0:3])		# 인덱스 0∼2 (3미만)
print(nums[:3])		# 인덱스 0∼2 (3미만)
print(nums[3:50])		# 인덱스 3∼49 (50미만)
print(nums[3:])		# 인덱스 3∼끝까지
print(nums[0:5:2])		# 인덱스 0∼4까지 2씩 증가
print(nums[:])		# 전체 리스트의 복사본
print(nums[::-1])		# 리스트 뒤집기
print(nums[:2] + nums[3:])	# 인덱스 0∼1 + 인덱스 3∼끝까지 

low = nums[:2]		# 0∼1 
high = nums[3:]		# 3∼끝까지 
print(low + high)		# 덧셈 연결

# [3] 가변(Mutable) 특성을 활용한 리스트 요소 변경 및 삭제
nums = [1, 2, 3, 4, 5, 6]
nums[2] = 20		# 인덱스 2번 요소를 20으로 변경
print(nums)

nums = [1, 2, 3, 4, 5, 6]
nums[1:3] = [10, 20]	# 인덱스 1,2번 요소를 10,20으로 변경
print(nums)

nums = [1, 2, 3, 4, 5, 6]
nums[1:3] = []		# 인덱스 1,2번 요소를 삭제
print(nums)
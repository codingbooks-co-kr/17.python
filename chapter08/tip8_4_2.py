# ② 리스트 요소/슬라이스 삭제
nums = [10, 20, 30, 40, 50]

del nums[1]	# 특정 인덱스의 요소 삭제
print(nums)	# 결과: [10, 30, 40, 50]

del nums[1:3]	# 특정 슬라이스 삭제
print(nums)	# 결과: [10, 50]

del nums		# 전체 리스트 삭제
#print(nums)	# 오류!

# ③ 딕셔너리의 키:값 쌍 삭제
student = {"name": "민수", "age": 20}

del student["age"]
print(student)	# 결과: {'name': '민수'}

del student	# 전체 딕셔너리 삭제
#print(student)	# 오류!
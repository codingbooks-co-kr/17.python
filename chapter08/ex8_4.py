# 딕셔너리 생성
student = {"name": "민수", "age": 20}
print(student)

# 새로운 항목(키:값) 추가
student["major"] = "컴퓨터공학"
print(student)

# 기존 키의 값 수정
student["age"] = 22 
print(student)

# 특정 항목(키:값) 삭제
del student["major"]		# 항목 삭제-1
#student.pop("major")	# 항목 삭제-2
print(student)

# 모든 항목 삭제
student = {}	# 모든 항목 삭제-1
#student.clear()	# 모든 항목 삭제-2
print(student)
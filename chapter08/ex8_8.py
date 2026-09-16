# 딕셔너리 생성
student = {"name": "민수", "age": 20}

# ❶ 기본적인 키 순회
for key in student:			# 키만 순회
    print("키:", key)

# ❷ keys()를 이용한 키 순회
for key in student.keys():		# 키만 순회
    print("키:", key)

# ❸ values()를 이용한 값 순회
for value in student.values():		# 값만 순회
    print("값:", value)

# ❹ items()를 이용한 키, 값 순회
for key, value in student.items():	# 키, 값 순회
    print(key, value)
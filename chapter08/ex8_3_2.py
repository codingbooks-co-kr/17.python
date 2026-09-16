# ❷ keys(), values(), items() → 리스트 변환

# 딕셔너리 생성
student = {"name": "민수", "age": 20}

# 딕셔너리의 키를 리스트 형식으로 조회
keys = list(student.keys())
print(keys)

# 딕셔너리의 값을 리스트 형식으로 조회
values = list(student.values())
print(values)

# 딕셔너리의 항목(키:값)을 리스트 변환 후 조회
items = list(student.items())
print(items)
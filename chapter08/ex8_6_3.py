# ❸ 키가 없다면 새로운 데이터 추가 (동적 업데이트)
student = {"name": "민수", "age": 20}
new_key = input("키 입력: ")
if new_key not in student:
    new_value = input("값 입력: ")
    student[new_key] = new_value
    print(student)
else:
    print(f"{new_key}: {student[new_key]} - 이미 정보가 존재함!")
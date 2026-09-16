# 딕셔너리 생성: {키:값, 키:값,...}
student = {
    "name": "민수",
    "age": 20,
    "major": "컴퓨터공학"
}

# 딕셔너리의 모든 항목(키:값) 조회
print(student)

# ❶키를 통해 값 조회 ([키] 사용)
print(student["name"])
print(student["age"])
print(student["major"])
#print(student["height"])		# 오류!

# ❷ 키를 통해 값 조회 (get(키) 사용)
print(student.get("name"))
print(student.get("age"))
print(student.get("major"))
print(student.get("height"))		# 오류없음
print(student.get("height", "없음"))	# 오류없음
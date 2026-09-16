# 리스트-딕셔너리 조합으로 학생별 정보 처리

students = [
    {"이름": "민수", "점수": 96, "등급": "A+"},
    {"이름": "지수", "점수": 82, "등급": "B"}
]

print("\n--- 요소 변경 전 학생별 정보1 ---")
print(students)

print("\n--- 요소 변경 전 학생별 정보2 ---")
for student in students:
    print(student["이름"], student["점수"], student["등급"])

print("\n--- 특정 학생의 정보 ---")
print(students[0])
print(students[1]["이름"])

# 추가: 새로운 학생 추가
new_student = {"이름": "진우", "점수": 85, "등급": "B+"}
students.append(new_student)

# 수정: 민수의 점수 변경
students[0]["점수"] = 100

# 삭제: 민수의 등급 삭제
del students[0]["등급"]

# 삭제: 두 번째 학생(지수) 전체 삭제
del students[1]

print("\n--- 요소 변경 후 학생별 정보 ---")
print(students)

print("\n--- 점수 합계 및 평균 ---")
total = 0
for student in students:
    total += student["점수"]
average = total / len(students)
print(f"합계: {total:.1f}, 평균: {average:.1f}")
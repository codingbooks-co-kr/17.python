# 중첩 리스트의 예: 학생 정보 관리

students = [	# 학생 정보(이름/학년/점수)의 초기화
    ["민수", 1, 90],
    ["지수", 3, 85],
    ["진우", 2, 78]
]

print("\n--- 학생별 정보 ---")
for student in students:
    print(f"이름: {student[0]}, {student[1]}학년, {student[2]}점")

print("\n--- 평균 점수 계산 ---")
total = 0
count = 0
for student in students:
    total += student[2]
    count += 1

average = total / count
print(f"평균 점수: {average:.1f}점")
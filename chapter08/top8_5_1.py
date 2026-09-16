# 중첩 딕셔너리로 학생별 정보 관리

students = {		# 학생별 세부 정보 초기화
    "민수": {
        "학년": 1,
        "나이": 20,
        "성별": "남",
        "점수": {"수학": 90, "영어": 85, "코딩": 75}
    },
    "지수": {
        "학년": 3,
        "나이": 22,
        "성별": "여",
        "점수": {"수학": 95, "영어": 90, "코딩": 85}
    }
}

print("\n--- 항목 변경 전 학생별 정보 ---")
print(students)

print("\n--- 특정 학생의 정보 ---")
print(students["민수"])
print(students["민수"]["나이"])
print(students["민수"]["점수"]["수학"])

# 추가: 새로운 학생 추가
students["진우"] = {"학년": 2, "나이": 23, "성별": "남", "점수": {"수학": 78, "영어": 80, "코딩": 95}}

# 수정: 민수의 학년 변경
students["민수"]["학년"] = 2

# 삭제: 민수의 코딩 점수 삭제
del students["민수"]["점수"]["코딩"]

print("\n--- 항목 변경 후 학생별 정보 ---")
print(students)

print("\n--- 특정 학생의 점수 합계 및 평균 ---")
scores = students["민수"]["점수"]
total = sum(scores.values())
average = total / len(scores)
print(f"이름: 민수, 합계: {total:.1f}, 평균: {average:.1f}")

print("\n--- 학생별 점수 합계 및 평균 ---")
for name, info in students.items():
    scores = info["점수"]
    total = sum(scores.values())
    average = total / len(scores)
    print(f"이름: {name}, 합계: {total:.1f}, 평균: {average:.1f}")

print("\n--- 학생별 세부 정보 출력 ---")
for name, info in students.items():
    print(f"{name}: {info['학년']}학년, {info['나이']}세, {info['성별']}")
    for subject, score in info["점수"].items():
        print(f"{name}의 {subject}: {score}점")
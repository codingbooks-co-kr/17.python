# 중첩 딕셔너리의 예: 학생별 과목 점수

scores = {				  # 학생별 과목 점수 초기화
    "민수": { "영어": 88, "수학": 75, "코딩": 92 },
    "지수": { "영어": 95, "수학": 88, "코딩": 74 }
}

print("\n--- 특정 정보에 접근/수정/삭제 ---")
print(f"민수의 점수: {scores['민수']}")		  # 특정 정보(민수의 점수)에 접근
print(f"민수의 원래 영어 점수: {scores['민수']['영어']}")

scores["민수"]["영어"] = 95			  # 특정 요소(민수의 영어 점수) 수정
print(f"민수의 수정 영어 점수: {scores['민수']['영어']}")

del scores["민수"]["코딩"]			  # 특정 요소(민수의 코딩 점수) 삭제
print(f"민수의 코딩 점수 삭제 후: {scores['민수']}")

print("\n--- 정보 추가 ---")
scores["진우"] = {"영어": 90, "수학": 80, "코딩": 83}	  # 특정 정보(진우의 점수) 추가
print(f"학생 추가 후: {scores}")

print("\n--- 특정 학생의 점수 합계 및 평균 ---")
total = sum(scores["민수"].values())		  # 민수의 점수 합계
average = total / len(scores["민수"])		  # 민수의 점수 평균
print(f"민수의 점수 합계: {total:.1f}, 평균: {average:.1f}점")

print("\n--- 학생별 점수 합계 및 평균 ---")
for name, subjects in scores.items():
    total = sum(subjects.values())
    average = total / len(subjects)
    print(f"이름: {name}, 합계: {total:.1f}, 평균: {average:.1f}")
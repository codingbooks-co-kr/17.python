# ❶ 점수에 따라 학점 평가 (중첩 조건부 표현식)

score = int(input("점수: "))
if score < 0 or score > 100:
    print("평가 불가!")
else:
    grade = ('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F')		# 괄호 () 생략 가능!
    print(f"학점: {grade}")
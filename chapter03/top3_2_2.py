# ❷ 점수에 따라 합격/불합격 평가 (조건부 표현식)

score = int(input("입력점수: "))
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")
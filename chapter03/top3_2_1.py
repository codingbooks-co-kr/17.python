# ❶ 점수에 따라 합격/불합격 평가 (if-else문)

score = int(input("입력점수: "))
if score >= 80:
    result = "합격"
else:
    result = "불합격"
print(f"점수: {score}, 결과: {result}")
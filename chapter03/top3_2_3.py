# ❸ 점수에 따라 합격/불합격 평가 (함수의 반환값이 조건부 표현식)

def check_pass(s):		# 함수(5장) 정의
    return "합격" if s >= 80 else "불합격"

score = int(input("입력점수: "))
result = check_pass(score)	# 함수(5장) 호출
print(f"점수: {score}, 결과: {result}")
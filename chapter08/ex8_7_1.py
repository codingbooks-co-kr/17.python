# ❶ 안전한 조회: 과목별 성적 조회

scores = {"영어": 90, "수학": 85}
subject = input("조회할 과목명: ")	# 괴목명 입력

# get(키, 기본값): 키가 없으면 기본값 반환
result = scores.get(subject, "등록되지 않은 과목!")
print(f"조회결과: {result}")
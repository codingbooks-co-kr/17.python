# ❷ 성적순으로 이름과 점수 함께 정렬하기
names = ["민수", "지수", "진우", "소라"]
scores = [85, 95, 70, 100]

# (점수, 이름) 튜플로 묶고 리스트 변환 (점수가 앞에 와야 정렬 가능)
combined = list(zip(scores, names))
print(combined)		# 튜플 묶음 확인용

# 내림차순 정렬 (점수가 높은 순서대로, [질문7.10] 참조)
combined.sort(reverse=True)

for score, name in combined:
    print(f"{name}: {score}점")
# 학생별 점수와 평균, 최고점 출력

names = ["민수", "지수", "진우"]
scores1 = [80, 95, 75]
scores2 = [85, 91, 88]

print("\n--- 학생별 점수 표시 ---")
for index, (name, s1, s2) in enumerate(zip(names, scores1, scores2), start=1):
    print(f"{index}번: {name}의 점수는 {s1}점, {s2}점")

print("\n--- 학생별 평균점수 및 최고점수 ---")
for index, (name, s1, s2) in enumerate(zip(names, scores1, scores2), start=1):
    average = (s1 + s2) / 2
    top_score = max(s1, s2)
    print(f"{index}번: {name}의 평균은 {average:.1f}점, 최고점은 {top_score}점")
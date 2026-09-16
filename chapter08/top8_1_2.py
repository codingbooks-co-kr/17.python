# 기존 딕셔너리에서 점수에 따라 학점(A,B,C,D,F) 부여 후 (이름, 학점) 쌍으로 새 딕셔너리 생성
scores = {"민수": 85, "지수": 95, "진우": 75}
result = {name: ('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F') for name, score in scores.items()}
print(result)
# ❷ 함수를 활용한 딕셔너리 함축 (추천 방식)
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 메인 코드
scores = {"민수": 85, "지수": 95, "진우": 75}
result = {name: get_grade(score) for name, score in scores.items()}
print(result)
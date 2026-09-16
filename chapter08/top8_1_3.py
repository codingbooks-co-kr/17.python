# ❶ if-elif-else 조건문을 사용한 방식
scores = {"민수": 85, "지수": 95, "진우": 75}
result = {}
for name, score in scores.items():
    if score >= 90:
        result[name] = 'A'
    elif score >= 80:
        result[name] = 'B'
    elif score >= 70:
        result[name] = 'C'
    elif score >= 60:
        result[name] = 'D'
    else:
        result[name] = 'F'
print(result)
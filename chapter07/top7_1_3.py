# (1) 기존의 if-elif-else 조건문을 사용한 방식

# ❶ 점수에 따라 "우수", "보통", "미흡" 반환
scores = [75, 55, 92, 45]
result = []
for score in scores:
    if score >= 80:
        grade = "우수"
    elif score >= 60:
        grade = "보통"
    else:
        grade = "미흡"
    result.append(grade)
print(result)

# ❷ 단어 길이에 따라 "길다", "보통", "짧다" 반환
words = "apple banana kiwi avocado"
result = []
for word in words.split():
    # 단어의 길이를 재서 등급 결정
    if len(word) >= 7:
        length = "길다"
    elif len(word) >= 5:
        length = "보통"
    else:
        length = "짧다"
    result.append(length)
print(result)
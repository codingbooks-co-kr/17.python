# (2) 함수 기반 리스트 함축 방식

# ❸ 점수에 따라 "우수", "보통", "미흡" 반환
def get_grade(score):
    if score >= 80:
        return "우수"
    elif score >= 60:
        return "보통"
    else:
        return "미흡"

scores = [75, 55, 92, 45]
result = [get_grade(score) for score in scores]
print(result)

# ❹ 단어 길이에 따라 "길다", "보통", "짧다" 반환
def get_word_length(word):
    if len(word) >= 7:
        return "길다"
    elif len(word) >= 5:
        return "보통"
    else:
        return "짧다"

words = "apple banana kiwi avocado"
result = [get_word_length(word) for word in words.split()]
print(result)
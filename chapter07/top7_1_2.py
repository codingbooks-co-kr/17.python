# ❶ 점수에 따라 "우수", "보통", "미흡" 판별
scores = [75, 55, 92, 45]
result = ["우수" if s >= 80 else "보통" if s >= 60 else "미흡" for s in scores]
print(result)

# ❷ 단어 길이에 따라 "길다", "보통", "짧다" 판별
words = "apple banana kiwi avocado"
result = ["길다" if len(w) >= 7 else "보통" if len(w) >= 5 else "짧다" for w in words.split()]
print(result)
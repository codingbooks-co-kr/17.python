# ❶ 0∼3의 숫자 중 짝수는 '짝수', 홀수는 '홀수'로 변환
result = ["짝수" if n%2==0 else "홀수" for n in range(4)]
print(result)

# ❷ 짝수는 2를 더하고, 홀수는 2를 뺀 결과로 변환
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = [n+2 if n % 2 == 0 else n-2 for n in nums]
print(result)

# ❸ 60점 이상이면 "합격" 나머지는 "불합격" 판별
scores = [75, 55, 92]
result = ["합격" if s >= 60 else "불합격" for s in scores]
print(result)

# ❹ 5자를 넘는 단어는 대문자로, 나머지는 소문자로 변환
fruits = ["Banana", "Kiwi", "Cherry"]
result = [w.upper() if len(w) >= 5 else w.lower() for w in fruits]
print(result)

# ❺ 단어의 길이에 따라 '짧다' 또는 '길다'로 분류
words = "apple banana kiwi avocado"
result = ["길다" if len(w) >= 5 else "짧다" for w in words.split()]
print(result)
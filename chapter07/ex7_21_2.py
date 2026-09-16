# ❻ 문장 속 긴 단어 추출: 길이가 6자 이상인 단어만 추출
words = "Hello Python Coding"
result = [w for w in words.split() if len(w) >= 6]
print(result)

# ❼ 특정 문자 시작 단어 추출: 특정 문자('p')로 시작하는 단어만 추출
words = "Hello Python Coding"
result = [w for w in words.split() if w.lower().startswith('p')]
print(result)

# ❽ 숫자만 추출: 문자열에서 숫자만 추출
words = "Apple price is 1,500 won in 2026"
result = [c for c in words if c.isdigit()]
print(result)

# ❾ 공백 제거: 문자열에서 공백이 아닌 문자만 추출
words = "P   y t h o n"
result = [c for c in words if c != " "]
print(result)

# ❿ 모음만 추출: 문자열에서 모음만 추출
words = "Hello Python Coding"
result = [c for c in words if c.lower() in "aeiou"]
print(result)
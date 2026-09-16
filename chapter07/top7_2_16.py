# 1∼5까지의 숫자를 제곱으로 한 튜플 생성
result = tuple(n**2 for n in range(1, 6))
print(result)

# 튜플 안에 튜플 요소 생성
result = tuple((n, n**2) for n in range(1, 4))
print(result)

# 문자열을 각 문자로 쪼갠 후 튜플 생성
word = "Python"
result = tuple(c for c in word)
print(result)

# 문자열 리스트를 대문자 튜플로 변환
words = ["Python", "Java", "c++"]
result = tuple((w.upper()) for w in words)
print(result)

# 1∼10까지의 숫자 중 짝수만 튜플로 생성
result = tuple(n for n in range(1, 11) if n % 2 == 0)
print(result)

# 문자열 리스트에서 'a'로 시작하는 요소 추출 후 튜플 생성
fruits = ["apple", "banana", "kiwi", "avocado"]
result = tuple(f for f in fruits if f.startswith("a"))
print(result)

# 0 이상이면 '양수' 나머지는 '음수'로 분류
nums = [-5, 10, -4, 7]
result = tuple("양수" if n >= 0 else "음수" for n in nums)
print(result)
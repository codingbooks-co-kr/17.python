# ❸ 문자열 리스트에 filter() 함수를 적용한 예
words = ["apple", "banana", "kiwi", "watermelon"]

# 문자열 리스트에서 'e'가 포함된 문자열만 필터링
result = filter(lambda word: 'e' in word, words)
print(list(result))

# 문자열 리스트의 요소 중 길이가 6 이상인 문자열만 필터링
result = filter(lambda word: len(word) >= 6, words)
print(list(result))
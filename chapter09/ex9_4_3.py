# ❸ 리스트와 튜플에 map() 함수를 적용한 예
names = ['Kim', 'Lee', 'Park']
scores = (90, 85, 75)

# 리스트와 튜플의 요소를 짝지어 f-string 문자열 생성
result = map(lambda n, s: f"{n}-{s}점", names, scores)
print(list(result))

# 리스트와 튜플의 요소를 짝지어 점수에 5를 더한 튜플 생성
result = map(lambda n, s: (n, s + 5), names, scores)
print(list(result))
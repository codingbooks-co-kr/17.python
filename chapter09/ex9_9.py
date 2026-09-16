names = ["민수", "지수", "진우"]
ages = [20, 22]
scores = [87, 75, 95]

# ❶ zip()으로 객체 생성 후 리스트 변환
result = zip(names, scores)
print(result)	# zip 객체
print(list(result))	# 객체→리스트 변환

# ❷ 길이가 다른 리스트 묶기 (→가장 짧은 길이에 맞춤)
result = zip(names, ages, scores)
print(list(result))	# 객체→리스트 변환

# ❸ zip() → dict()을 통해 딕셔너리 변환
result = dict(zip(names, scores))
print(result)

# ❹ for문에서 zip()을 사용하지 않는 경우 (비추천)
for i in range(len(names)):
    print(names[i], scores[i])

# ❺ for문에서 zip()을 사용한 경우-1 (추천)
for name, score in zip(names, scores):
    print(name, score)

# ❻ for문에서 zip()을 사용한 경우-2 (→가장 짧은 길이에 맞춤)
for name, age, score in zip(names, ages, scores):
    print(name, age, score)

# ❼ for문에서 zip()을 사용한 경우-3 (참고)
for item in zip(names, ages, scores):
    print(item)
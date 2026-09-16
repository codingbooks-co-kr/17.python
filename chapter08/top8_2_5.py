# ❶ 0~5의 수를 제곱 (순서없음)
result = {x**2 for x in range(6)}
print(result)

# ❷ 리스트에서 중복 숫자 제거 (순서없음, 중복제거)
nums = [5, 1, 2, 2, 3, 3, 4, 4, 5]
result = {x for x in nums}
print(result)

# ❸ 딕셔너리에서 값만 모아 세트 생성 (순서없음, 중복제거)
scores = {"민수": 85, "지수": 92, "진우": 85}
result = {score for score in scores.values()}
print(result)
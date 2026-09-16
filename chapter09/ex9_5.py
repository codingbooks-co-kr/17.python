scores = [72, 85, 55, 95, 48]

# ❶ 점수 리스트의 점수가 60 이상이면 'Pass' 그렇지 않으면 'Fail' 변환
result = map(lambda s: 'Pass' if s >= 60 else 'Fail', scores)
print(list(result))		# 실행결과: ['Pass', 'Pass', 'Fail', 'Pass', 'Fail']

# ❷ 점수 리스트의 점수가 짝수이면 +10 그렇지 않으면 원 점수 그대로 변환
result = map(lambda s: s + 10 if s % 2 == 0 else s, scores)
print(list(result))		# 실행결과: [82, 85, 55, 95, 58]

words = ["apple", "banana", "kiwi", "watermelon"]

# ❸ 문자열 리스트의 길이가 6 이상이면 'Long', 그렇지 않으면 'Short' 변환
result = map(lambda w: 'Long' if len(w) >= 6 else 'Short', words)
print(list(result))		# 실행결과: ['Short', 'Long', 'Short', 'Long']

# ❹ 문자열 리스트의 'a'를 포함하면 'A' 변환, 그렇지 않으면 대문자 변환
result = map(lambda w: "A" if 'a' in w else w.upper(), words)
print(list(result))		# 실행결과: ['A', 'A', 'KIWI', 'A']

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

# ❺ nums1의 요소가 짝수이면 두 요소를 더하고, 홀수이면 두 요소를 곱함
result = map(lambda x, y: x + y if x % 2 == 0 else x * y, nums1, nums2)
print(list(result))		# 실행결과: [5, 8, 21, 12]

# ❻ 두 리스트의 요소별 합이 10 이상이면 'High', 그렇지 않으면 'Low' 변환
result = map(lambda x, y: 'High' if x + y >= 10 else 'Low', nums1, nums2)
print(list(result))		# 실행결과: ['Low', 'Low', 'High', 'High']
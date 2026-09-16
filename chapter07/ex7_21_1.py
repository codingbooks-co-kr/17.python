# ❶ 짝수만 추출: 1∼10까지의 숫자 중 짝수만 포함하는 리스트 생성
result = [n for n in range(1, 11) if n % 2 == 0]
print(result)

# ❷ 양수만 추출: 음수를 제거한 새로운 리스트 생성
nums = [1, -2, 3, -4, 5, 6, -7, 8, 9]
result = [n for n in nums if n > 0]
print(result)

# ❸ 긴 단어 추출: 길이가 5 이상인 단어만 추출한 새로운 리스트 생성
words = ["python", "java", "javascript", "c++", "c#"]
result = [w for w in words if len(w) >= 5]
print(result)

# ❹ 'c' 포함 단어 추출: 'c'를 포함하는 단어만 추출 후 대문자로 변환
words = ["python", "java", "javascript", "c++", "c#"]
result = [w.upper() for w in words if 'c' in w]
print(result)

# ❺ 확장자 필터링: '.txt' 확장자를 가진 파일명만 추출
filenames = ["a.txt", "b.png", "c.pdf", "d.txt"]
result = [f for f in filenames if f.endswith('.txt')]
print(result)
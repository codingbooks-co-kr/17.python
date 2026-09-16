# 문자열 시작과 끝에 공백 2개씩 포함
words = "  Just Do It, You Can Do It.  "

# count(): "o"의 출현 횟수(3) 반환
print(words.count("o"))

# count(): "Do"의 출현 횟수(2) 반환
print(words.count("Do"))

# count(): 인덱스 0∼20에서 "o"의 출현 횟수(2) 반환
print(words.count("o", 0, 20))

# index(): "u"가 처음 출현하는 인덱스(3) 반환
print(words.index("u"))

# find(): "Do"가 처음 출현하는 인덱스(7) 반환
print(words.find("Do"))

# find(): "Python"의 첫 출현 인덱스 반환, 찾지 못하면 –1
print(words.find("Python"))

# "Just"로 시작하는지 여부, 공백으로 시작하므로 False 반환
print(words.startswith("Just"))

# "."으로 끝나는지 여부, 공백으로 끝나므로 False 반환
print(words.endswith("."))

# replace(): "a"를 "A"로 교체한 새로운 문자열 반환
print(words.replace("a", "A"))

# upper(): 문자열의 모든 문자를 대문자로 변환
print(words.upper())

# lower(): 문자열의 모든 문자를 소문자로 변환
print(words.lower())

# strip(): 앞뒤 공백 제거
print(words.strip())

# join(): 모든 글자 사이에 "-" 넣기
print("-".join(words))

# split(): 공백 기준으로 문자열 분리(7개 요소) 후 리스트로 반환
print(words.split())

# split(): "," 기준으로 문자열 분리(2개 요소) 후 리스트로 반환
print(words.split(","))

# 공백 기준으로 문자열 분리(split) 후 정렬(sorted)
print(sorted(words.split()))
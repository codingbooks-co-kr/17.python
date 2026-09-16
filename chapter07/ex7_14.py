words = "apple banana kiwi watermelon"

# ❶ 변환: 문자열→공백 기준 단어 리스트→요소 순회하며 대문자로 변환
result = []  			# 빈 리스트 생성
for w in words.split():  		# 문자열→단어 리스트→요소 순회
    result.append(w.upper()) 		# 대문자로 변환, 리스트에 추가
print(result)

# ❷ 필터링: 문자열→공백 기준 단어 리스트→요소 순회, 6자 이상 단어만 추출
result = []  			# 빈 리스트 생성
for w in words.split():  		# 문자열→단어 리스트→요소 순회
    if len(w) >= 6:      		# 단어의 길이가 6자 이상이면
        result.append(w) 		# 리스트에 단어를 추가
print(result)

# ❸ 매칭: 문자열→공백 기준 단어 리스트→요소 순회, 'b'로 시작 단어 추출
result = []  			# 빈 리스트 생성
for w in words.split():  		# 문자열→단어 리스트→요소 순회
    if w.lower().startswith('b'): 	# 소문자 변환→'b'로 시작?
        result.append(w) 		# 리스트에 단어 추가
print(result)

# ❹ 분류: 문자열→공백 기준 단어 리스트→요소 순회, 단어 길이에 따라 분류
result = []  			# 빈 리스트 생성
for w in words.split():		# 문자열→단어 리스트→요소 순회
    if len(w) <= 5:  		# 길이가 5 이하이면
        result.append("짧다")		# '짧다'를 리스트에 추가
    elif len(w) <= 7: 		# 5 초과 7 이하이면
        result.append("보통")		# '보통'을 리스트에 추가
    else:            		# 7 초과이면
        result.append("길다")		# '길다'를 리스트에 추가
print(result)
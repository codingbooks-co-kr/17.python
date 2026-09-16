# ❹ 숫자를 문자로 변환: 숫자 요소 중 짝수는 '짝수', 홀수는 '홀수'로 변환
result = []  			# 빈 리스트 생성
for n in range(4):  			# 0부터 3까지의 숫자 요소를 순회
    if n % 2 == 0:  		# 숫자가 짝수이면
        result.append("짝수")
    else:           		# 숫자가 홀수이면
        result.append("홀수")
print(result)

# ❺ 숫자 데이터 일괄 수정: 짝수는 2를 더하고, 홀수는 2를 뺀 결과로 변환
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = []  			# 빈 리스트 생성
for n in nums:  			# 리스트의 숫자 요소를 순회
    if n % 2 == 0:       		# 숫자가 짝수이면
        result.append(n + 2)
    else:                		# 숫자가 홀수이면
        result.append(n - 2)
print(result)

# ❻ 문자열 리스트 가공: 5자를 넘는 단어는 대문자로, 나머지는 소문자로 변환
fruits = ["Apple", "Kiwi", "Cherry"]
result = []  			# 빈 리스트 생성
for f in fruits:       		# 리스트의 단어 요소를 순회
    if len(f) >= 5:         		# 단어의 길이가 5 이상이면
        result.append(f.upper()) 	# 대문자로 변환 후 추가
    else:                   		# 단어의 길이가 5 미만이면
        result.append(f.lower()) 	# 소문자로 변환 후 추가
print(result)
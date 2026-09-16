# 문자열의 인덱싱(Indexing), 슬라이싱(Slicing)

words = "Python Coding"

# [1] 인덱싱(Indexing)으로 한 글자 꺼내기
print(words[0])		# 인덱스 0번 문자
print(words[5])		# 인덱스 5번 문자
print(words[-1])		# 끝문자
print(words[-5])		# 끝에서 5번째 문자

# [2] 슬라이싱(Slicing)으로 범위 잘라내기 [시작:끝:간격]
print(words[0:3])		# 인덱스 0∼2 (3미만)
print(words[:3])		# 인덱스 0∼2 (3미만)
print(words[8:50])		# 인덱스 8∼49 (50미만)
print(words[0:9:2])		# 인덱스 0∼8까지 2씩증가
print(words[8:])		# 인덱스 8∼끝까지
print(words[:])		# 문자열의 전체 복사본
print(words[::-1])		# 문자열 뒤집기

# 슬라이싱 조각들을 더하기(+) 연산자로 연결하기
print(words[:5] + words[5:])  	# Python Coding
print(words[:3] + words[10:]) 	# "Pyt" + "ing"
low = words[:6]		# 0∼5: "Python"
high = words[7:]		# 7∼끝까지: "Coding"
print(low, high)
print(low + high)		# 덧셈 연결

# 문자 변경 불가 (리스트에서는 변경 가능)
# words[0] = 'H'		# 오류!

# 문자를 변경하고 싶다면 다음처럼 '새로운 문자열' 생성
print('H' + words[1:])	# 새로운 문자열 생성
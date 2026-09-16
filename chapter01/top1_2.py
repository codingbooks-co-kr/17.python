# 문자와 유니코드의 상호 변환 

# 1. 유니코드 이스케이프 시퀀스로 문자 출력하기
print('\u0041')	# 유니코드 U+0041: 'A' (ASCII와 동일)
print('\uAC00')	# 유니코드 U+AC00은 '가'
print('\uD7A3')	# 유니코드 U+D7A3은 '힣'

# 2. ord(): 문자를 유니코드 정수(10진수)로 변환
print(ord('A'))	# 65 (=0x41: 'A'의 유니코드, ASCII와 동일)
print(ord('가'))	# 44032 (=0xAC00: 한글 '가'의 유니코드)
print(ord('힣'))	# 55203 (=0xD7A3: 한글 '힣'의 유니코드)

# 3. chr(): 숫자를 유니코드 문자로 변환
print(chr(65))	# 또는 print(chr(0x41))
print(chr(44032))	# 또는 print(chr(0xAC00))
print(chr(55203))	# 또는 print(chr(0xD7A3))
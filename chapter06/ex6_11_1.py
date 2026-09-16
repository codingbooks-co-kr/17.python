# 문자열 관련 다양한 메서드: 알파벳/숫자/공백/소문자/대문자 여부 판단

print("Python123".isalnum())		# 알파벳(유니코드문자)/숫자이면 True
print("파이썬123".isalnum())		# 알파벳(유니코드문자)/숫자이면 True

print("Python".isalpha())		# 알파벳(유니코드문자)이면 True
print("파이썬".isalpha())		# 알파벳(유니코드문자)이면 True
print("12345".isalpha())		# 빈문자열/숫자/공백/특수문자: False

print("12345".isdigit())		# 숫자이면 True
print(" ".isspace())			# 공백문자이면 True
print("python".islower())		# 소문자이면 True
print("PYTHON".isupper())		# 대문자이면 True
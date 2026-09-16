# 다양한 진법의 숫자 출력

decimal_num = 255
print(decimal_num)		# 10진수 출력
print(bin(decimal_num))	# 10진수→2진수 문자열로 변환
print(hex(decimal_num))	# 10진수→16진수 문자열로 변환

binary_num = 0b11111111	# 2진수 리터럴 (앞에 0b를 붙임)
print(binary_num)		# 2진수→10진수로 변환되어 출력

hex_num = 0xFF		# 16진수 리터럴 (앞에 0x를 붙임)
print(hex_num)		# 16진수→10진수로 변환되어 출력
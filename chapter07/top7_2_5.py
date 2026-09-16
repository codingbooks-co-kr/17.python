# 튜플 요소가 1개일 때 콤마 필수
num = (10,)		# 튜플
#num = 10,		# 괄호생략가능, 콤마필수
print(num, type(num))

# 괄호가 있지만 콤마가 없으면 정수로 취급
num = (10)		# 콤마가 없으면 정수 10
print(num, type(num))